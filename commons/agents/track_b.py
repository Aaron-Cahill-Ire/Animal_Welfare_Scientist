"""Bounded applied research helpers; drafts and observations require human review.

B4's synthetic video format is a sequence of timestamped grayscale frames,
with pixel intensities in [0,255]. No compressed-video decoder or audio backend
is implied. B5 uses a fixed, inspectable script and never executes supplied code.
"""
import datetime as dt
import json
import math
import statistics


def result(data, status="completed", warnings=None, required_action=None):
    answer = {"status": status, "data": data, "warnings": warnings or []}
    if required_action:
        answer["required_action"] = required_action
    return answer


def numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _b1(p):
    brief = p["brief"]
    intervention, outcome = brief.get("intervention"), brief.get("outcome")
    comparator, population, duration = (brief.get(k) for k in ("comparator", "population", "duration"))
    missing = [k for k in ("intervention", "outcome", "comparator", "population", "duration", "minimum_effect") if brief.get(k) is None]
    if not intervention or not outcome:
        return result({"hypotheses": [], "unresolved_decisions": missing}, "abstained", required_action="Specify intervention or measurement and observable outcome.")
    effect = brief.get("minimum_effect")
    if not numeric(effect) or effect <= 0:
        missing.append("positive numeric minimum_effect")
    prior = brief.get("prior_probability")
    if prior is not None and (not numeric(prior) or not 0 <= prior <= 1):
        prior = None
        missing.append("prior_probability between zero and one")
    return result({
        "hypotheses": [{"claim": f"In {population or '[population unresolved]'}, {intervention} changes {outcome} compared with {comparator or '[comparator unresolved]'} over {duration or '[duration unresolved]' }.",
                        "minimum_effect": effect, "direction": brief.get("direction", "unspecified"),
                        "falsifier": f"A sufficiently precise comparison incompatible with the predefined direction and minimum effect on {outcome}.", "test_ready": not missing and brief.get("direction") in ("increase", "decrease")}],
        "theory_of_change": [intervention, brief.get("mechanism", "Mechanism unresolved"), outcome],
        "competing_explanations": ["Baseline group differences", "Measurement drift or observer effects", "Time trends unrelated to the intervention"],
        "assumptions": brief.get("assumptions", []) + ["Indicator changes may not establish welfare changes", "Comparison must control credible competing explanations"],
        "belief_forecast": {"probability": prior, "basis": "User-supplied prior; not estimated from the brief" if prior is not None else "No valid calibrated prior supplied"},
        "evidence_that_would_change_conclusion": [f"Independent replication measuring {outcome}", "Evidence that the indicator does not measure the intended construct", "Adequately powered null or opposite-direction results"],
        "unresolved_decisions": missing + ([] if brief.get("direction") in ("increase", "decrease") else ["direction"])
    }, "partial", ["Hypothesis draft; causal and welfare claims remain unvalidated."])


def _b2(p):
    h, fw = p["hypothesis"], p["framework"]
    indicators = []
    for item in fw.get("indicators", []):
        if not isinstance(item, dict):
            continue
        same_context = item.get("validation_population") == h.get("population") and bool(h.get("population"))
        indicators.append({"name": item.get("name"), "unit": item.get("unit"), "construct": item.get("construct"), "source_id": item.get("source_id"),
                           "validation_status": "user_reported_context_match" if same_context and item.get("source_id") else "unverified_context_transfer",
                           "procedure": item.get("procedure", "Specify collection procedure"), "gold_standard": item.get("gold_standard")})
    missing = [k for k in ("population", "comparator", "outcome", "duration") if not h.get(k)]
    missing += ["aggregation across indicators and time", "sampling schedule", "adverse event and humane stopping rules", "allocation and blinding"]
    if not indicators:
        missing.append("framework indicators and validation evidence")
    return result({"protocol_draft": {"framework": fw.get("name", "Unnamed user framework"), "population": h.get("population"), "hypothesis": h,
                                     "indicators": indicators, "procedures": [i["procedure"] for i in indicators],
                                     "aggregation": "Unresolved; no default welfare score is computed"},
                   "unresolved_decisions": missing,
                   "review_needs": ["Qualified researcher review", "Ethics review before any animal study", "Construct validity and species/context transfer review"]},
                  "awaiting_human", ["A source reference and matching population do not independently validate an indicator."], "Obtain qualified researcher and ethics approval before conducting the protocol.")


def _b3(p):
    protocol, resources = p["protocol"], p["resources"]
    randomized = resources.get("randomization_feasible") is True
    unit = protocol.get("experimental_unit")
    available = resources.get("available_units")
    effect, sd = resources.get("minimum_effect"), resources.get("outcome_sd")
    alpha, power = resources.get("alpha", 0.05), resources.get("power", 0.8)
    estimate = None
    if all(numeric(v) for v in (effect, sd, alpha, power)) and effect > 0 and sd > 0 and 0 < alpha < 1 and .5 < power < 1:
        z_alpha = statistics.NormalDist().inv_cdf(1-alpha/2)
        z_power = statistics.NormalDist().inv_cdf(power)
        estimate = math.ceil(2 * (z_alpha + z_power)**2 * sd**2 / effect**2)
    missing = [k for k in ("experimental_unit", "comparator", "primary_outcome") if not protocol.get(k)]
    if estimate is None:
        missing.append("valid positive minimum_effect/outcome_sd and alpha/power")
    if protocol.get("clustered"):
        missing.append("cluster count, cluster sizes and intra-cluster correlation; simple sample estimate is inapplicable")
        estimate = None
    feasible = (2*estimate <= available) if estimate is not None and numeric(available) else None
    return result({"design": "parallel randomized comparison" if randomized else "observational comparison; confounding unresolved", "experimental_unit": unit,
                   "comparator": protocol.get("comparator"), "sampling": {"available_units": available, "approximate_units_per_arm": estimate,
                   "resource_feasible": feasible, "formula": "ceil(2*(z_(1-alpha/2)+z_power)^2*sd^2/effect^2)",
                   "assumptions": ["Independent units", "Two equally sized groups", "Continuous approximately normal outcome", "No attrition, clustering or multiplicity adjustment", "Large-sample approximation; statistician review required"]},
                   "power_inputs": {"minimum_effect": effect, "outcome_sd": sd, "alpha": alpha, "power": power},
                   "analysis_plan": {"confirmatory": {"outcome": protocol.get("primary_outcome"), "contrast": "between-group mean difference", "prespecification_required": True},
                                     "exploratory": protocol.get("secondary_outcomes", []), "missing_data": "Report missingness by group; prespecify handling and sensitivity analysis"},
                   "stopping_assumptions": ["No efficacy peeking without prespecified sequential boundaries", "Human-approved humane stopping rules override study completion"],
                   "unresolved_decisions": missing}, "partial", ["Planning approximation only; do not start a study from this output."])


def _b4(p):
    video = p["video"]
    if video.get("format") != "synthetic-grayscale-frames-v1" or video.get("audio"):
        return result({"annotations": [], "backend": "native-python-frame-differences"}, "unsupported_input", ["Only synthetic grayscale frame sequences are supported; audio and encoded video are unsupported."], "Supply format synthetic-grayscale-frames-v1 with timestamped grayscale pixel arrays and no audio.")
    frames = video.get("frames", [])
    if not isinstance(frames, list) or not 2 <= len(frames) <= 120:
        return result({"annotations": []}, "abstained", required_action="Supply 2–120 frames, each at most 64 by 64 pixels, covering at most 60 seconds.")
    annotations, previous, shape, last_t, first_t = [], None, None, None, None
    for frame in frames:
        if not isinstance(frame, dict):
            return result({"annotations": []}, "abstained", required_action="Each frame must contain timestamp_seconds and pixels.")
        timestamp, rows = frame.get("timestamp_seconds"), frame.get("pixels")
        valid = isinstance(rows, list) and 1 <= len(rows) <= 64 and all(isinstance(row, list) and 1 <= len(row) <= 64 for row in rows)
        if not valid or not numeric(timestamp) or timestamp < 0 or (last_t is not None and timestamp <= last_t):
            return result({"annotations": []}, "abstained", required_action="Provide finite increasing nonnegative timestamps and nonempty rectangular pixel arrays.")
        current_shape = (len(rows), len(rows[0]))
        flat = [v for row in rows for v in row]
        if any(len(row) != current_shape[1] for row in rows) or (shape and current_shape != shape) or any(not numeric(v) or not 0 <= v <= 255 for v in flat):
            return result({"annotations": []}, "abstained", required_action="Frames must share rectangular dimensions and finite pixel intensities from 0 to 255.")
        first_t = timestamp if first_t is None else first_t
        if timestamp-first_t > 60:
            return result({"annotations": []}, "abstained", required_action="Clip the synthetic sequence to at most 60 seconds.")
        change = None if previous is None else sum(abs(a-b) for a,b in zip(previous, flat))/len(flat)
        annotations.append({"timestamp_seconds": timestamp, "mean_brightness": statistics.mean(flat), "mean_absolute_pixel_change": change,
                            "observation": "initial frame" if change is None else ("no pixel change" if change == 0 else "pixel intensities changed"),
                            "uncertainty": "Pixel change can reflect lighting, camera or object motion; no animal identity, behaviour or welfare inference."})
        previous, shape, last_t = flat, current_shape, timestamp
    return result({"annotations": annotations, "backend": "native-python-frame-differences", "duration_seconds": last_t-first_t,
                   "annotation_format": "timestamped-descriptive-json-v1", "welfare_diagnosis": None}, warnings=["Synthetic frame analysis only; no validated behaviour classifier or human-labelled welfare evaluation."])


# Fixed script: embedded JSON is parsed as data and no user code is interpolated.
_STATS_SCRIPT = '''import json, math, statistics
payload = json.loads(PAYLOAD_JSON)
rows = payload["rows"]
stats = {}
for column in payload["columns"]:
    raw = [row.get(column) for row in rows]
    values = [v for v in raw if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)]
    missing = sum(v is None for v in raw)
    stats[column] = {"n": len(values), "missing": missing, "invalid": len(raw)-missing-len(values),
                     "missing_fraction": missing/len(rows) if rows else None,
                     "mean": statistics.mean(values) if values else None,
                     "median": statistics.median(values) if values else None,
                     "sample_sd": statistics.stdev(values) if len(values)>1 else None,
                     "min": min(values) if values else None, "max": max(values) if values else None}
print(json.dumps(stats, sort_keys=True))
'''


def _b5(p):
    rows, columns = p["rows"], p["columns"]
    if len(rows) > 10000 or not columns or len(columns) > 100 or any(not isinstance(r, dict) for r in rows) or any(not isinstance(c, str) for c in columns):
        return result({"statistics": {}}, "abstained", required_action="Supply up to 10000 row objects and 1–100 numeric column names.")
    stats = {}
    for column in columns:
        raw = [row.get(column) for row in rows]
        values = [v for v in raw if numeric(v)]
        missing = sum(v is None for v in raw)
        stats[column] = {"n": len(values), "missing": missing, "invalid": len(raw)-missing-len(values),
                         "missing_fraction": missing/len(rows) if rows else None,
                         "mean": statistics.mean(values) if values else None, "median": statistics.median(values) if values else None,
                         "sample_sd": statistics.stdev(values) if len(values)>1 else None,
                         "min": min(values) if values else None, "max": max(values) if values else None}
    script = "PAYLOAD_JSON = " + repr(json.dumps({"rows": rows, "columns": columns})) + "\n" + _STATS_SCRIPT
    causal = p.get("causal_assumptions", {})
    all_assumptions = ["exchangeability", "positivity", "consistency", "no_interference", "temporal_order", "measurement_validity"]
    missing_assumptions = [k for k in all_assumptions if not causal.get(k)]
    return result({"question": p["question"], "statistics": stats, "reproducible_script": script,
                   "analysis_method": "Available finite numeric values per column; sample standard deviation uses n-1; no imputation",
                   "causal_assessment": {"causal_effect_estimated": False, "conclusion": "Descriptive summaries do not establish causation",
                                         "user_asserted_assumptions": causal, "unresolved_assumptions": missing_assumptions,
                                         "sensitivity_needs": ["Missing-not-at-random sensitivity", "Unmeasured confounding assessment", "Measurement error assessment"]}},
                  "partial" if not rows or any(s["n"] == 0 or s["invalid"] or s["missing"] for s in stats.values()) else "completed",
                  ["Missingness mechanism is unknown; available-case statistics may be biased. Independent statistical review required for consequential use."])


def _b6(p):
    requirements = p["requirements"]
    components, interfaces, tests, unresolved = [], [], [], []
    mapping = {"temperature": ("temperature sensor", "digital or analog signal"), "mass": ("load cell and amplifier", "calibrated analog/ADC signal"),
               "motion": ("camera or inertial sensor", "timestamped digital samples"), "sound": ("microphone and ADC", "sampled audio"),
               "light": ("photodiode and ADC", "calibrated light samples")}
    for i, req in enumerate(requirements):
        if not isinstance(req, dict):
            unresolved.append(f"Requirement {i}: provide an object")
            continue
        rid = req.get("id", f"requirement-{i+1}")
        kind, quantity = req.get("kind"), req.get("quantity")
        if kind == "measurement" and quantity in mapping:
            cls, interface = mapping[quantity]
        elif kind == "intervention":
            cls, interface = "actuator with independent fail-safe and hardware cutoff", "bounded command and independent feedback"
            unresolved.append(f"{rid}: actuation limits, safe state and qualified safety review")
        else:
            unresolved.append(f"{rid}: unsupported kind/quantity; select sensor with an engineer")
            continue
        components.append({"requirement_id": rid, "class": cls, "purpose": kind, "quantity": quantity})
        interfaces.append({"requirement_id": rid, "signal": interface, "connector": req.get("connector"), "voltage": req.get("voltage")})
        tests.append({"requirement_id": rid, "test": "Bench calibration against a reference and repeated measurements" if kind == "measurement" else "Bench-only actuation limit, power-loss safe-state and cutoff tests",
                      "acceptance": req.get("acceptance"), "animal_use": False})
        if not req.get("acceptance"):
            unresolved.append(f"{rid}: measurable acceptance threshold")
    return result({"concept_specification": {"components": components, "interfaces": interfaces, "environment": p.get("environment", {}), "production_ready": False},
                   "bench_test_plan": tests, "unresolved_decisions": unresolved, "review_needs": ["Engineering review", "Animal ethics review before any animal use"]},
                  "partial" if components else "abstained", ["Component classes only; electrical compatibility and safety are not certified. CAD generation unsupported."])


def _date(value):
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date() if "T" in value else dt.date.fromisoformat(value)
    except (ValueError, TypeError, AttributeError):
        return None


def _b7(p):
    requirements, records = p["requirements"], p["supplier_records"]
    today = _date(p.get("as_of"))
    max_age = p.get("max_age_days", 30)
    if today is None or not numeric(max_age) or max_age < 0:
        return result({"candidates": []}, "abstained", required_action="Supply a valid as_of date and nonnegative max_age_days.")
    candidates, rejected = [], []
    for record in records:
        if not isinstance(record, dict):
            continue
        if record.get("approved") is not True:
            rejected.append({"part_id": record.get("part_id"), "reason": "Supplier record is not approved"})
            continue
        gaps, conflicts = [], []
        for key, wanted in requirements.items():
            actual = record.get("specifications", {}).get(key)
            if actual is None:
                gaps.append(key)
            elif actual != wanted:
                conflicts.append({"field": key, "required": wanted, "actual": actual})
        checked = _date(record.get("checked_at"))
        age = (today-checked).days if checked else None
        freshness = "unknown" if age is None else "future_timestamp" if age < 0 else "stale" if age > max_age else "within_requested_age"
        candidates.append({"part_id": record.get("part_id"), "supplier": record.get("supplier"), "source_id": record.get("source_id"), "url": record.get("url"),
                           "compatibility": "conflict" if conflicts else "unknown" if gaps else "matches_supplied_constraints", "gaps": gaps, "conflicts": conflicts,
                           "checked_at": record.get("checked_at"), "age_days": age, "freshness": freshness,
                           "cost": record.get("cost"), "currency": record.get("currency"), "availability": record.get("availability"), "lead_time_days": record.get("lead_time_days"),
                           "independent_confirmation_required": True})
    return result({"candidates": candidates, "rejected": rejected, "as_of": p["as_of"], "constraint_method": "Exact equality against user-supplied specification fields; no inferred substitutes"},
                  "partial" if candidates else "abstained", ["No live procurement lookup. Cost and availability are user-supplied, dated claims; confirm before purchase."])


def _b8(p):
    criteria, observations = p["criteria"], p["results"]
    evaluations = []
    for c in criteria:
        cid, metric, op, threshold = c.get("id"), c.get("metric"), c.get("operator"), c.get("threshold")
        matches = [r for r in observations if r.get("metric") == metric]
        verdict, reason, value = "indeterminate", "Missing or ambiguous measurement", None
        if len(matches) == 1:
            r = matches[0]
            value = r.get("value")
            if not metric or not numeric(value) or not numeric(threshold):
                reason = "Missing or nonnumeric value/threshold"
            elif c.get("unit") != r.get("unit") or not c.get("unit"):
                reason = "Missing or incompatible measurement units"
            elif op not in ("<=", ">=", "<", ">", "=="):
                reason = "Unsupported comparison operator"
            else:
                passed = {"<=": value <= threshold, ">=": value >= threshold, "<": value < threshold, ">": value > threshold, "==": value == threshold}[op]
                verdict, reason = ("pass" if passed else "fail"), "Compared supplied measurement with predefined threshold"
        evaluations.append({"criterion_id": cid, "metric": metric, "value": value, "threshold": threshold, "operator": op, "status": verdict, "reason": reason, "critical": c.get("critical", False)})
    if any(e["status"] == "fail" and e["critical"] for e in evaluations):
        recommendation = "stop"
    elif not evaluations or any(e["status"] in ("fail", "indeterminate") for e in evaluations):
        recommendation = "revise"
    elif p.get("unexpected_outcomes"):
        recommendation = "revise"
    else:
        recommendation = "advance"
    belief = p.get("belief", {})
    prior, lr = belief.get("prior_probability"), belief.get("likelihood_ratio")
    posterior = None
    if numeric(prior) and 0 < prior < 1 and numeric(lr) and lr > 0 and belief.get("assumptions"):
        odds = prior/(1-prior)*lr
        posterior = odds/(1+odds)
    return result({"criteria": evaluations, "recommendation": recommendation, "recommendation_scope": "Human-reviewed next bench stage only; no animal deployment authorization",
                   "deviations": [e for e in evaluations if e["status"] != "pass"], "unexpected_outcomes": p.get("unexpected_outcomes", []),
                   "belief_update": {"prior_probability": prior, "posterior_probability": posterior, "likelihood_ratio": lr,
                                     "assumptions": belief.get("assumptions", []), "basis": "User-supplied likelihood ratio and assumptions; no automatic inference from passing criteria"}},
                  "awaiting_human", ["Bench pass does not establish animal welfare benefit, field performance or safety."], "Review deviations, evidence quality and recommendation before advancing.")


_EXAMPLES = {
    "B1": {"brief": {"intervention": "quieter synthetic enclosure", "outcome": "sound level", "population": "synthetic enclosure", "comparator": "standard enclosure", "duration": "one hour", "direction": "decrease", "minimum_effect": 3}},
    "B2": {"hypothesis": {"population": "synthetic enclosure", "outcome": "sound level", "comparator": "standard enclosure", "duration": "one hour"}, "framework": {"name": "User-supplied environmental measurement framework", "indicators": [{"name": "sound level", "unit": "dB", "construct": "environmental noise", "procedure": "Record calibrated readings at predefined positions", "source_id": "synthetic-protocol", "validation_population": "synthetic enclosure"}]}},
    "B3": {"protocol": {"experimental_unit": "synthetic enclosure", "comparator": "standard enclosure", "primary_outcome": "sound level"}, "resources": {"available_units": 100, "minimum_effect": 2, "outcome_sd": 3, "randomization_feasible": True}},
    "B4": {"video": {"format": "synthetic-grayscale-frames-v1", "frames": [{"timestamp_seconds": 0, "pixels": [[0, 0], [0, 0]]}, {"timestamp_seconds": 1, "pixels": [[10, 10], [10, 10]]}]}},
    "B5": {"rows": [{"reading": 1}, {"reading": 3}, {"reading": None}], "columns": ["reading"], "question": "What is the distribution of synthetic readings?"},
    "B6": {"requirements": [{"id": "r1", "kind": "measurement", "quantity": "temperature", "acceptance": "error <= 0.5 C against reference"}], "environment": {"location": "synthetic bench"}},
    "B7": {"requirements": {"voltage": 3.3}, "supplier_records": [{"part_id": "synthetic-part", "supplier": "Synthetic supplier", "approved": True, "specifications": {"voltage": 3.3}, "checked_at": "2026-09-01", "cost": 12, "currency": "USD", "availability": "synthetic in-stock claim", "source_id": "synthetic-catalogue"}], "as_of": "2026-09-13"},
    "B8": {"criteria": [{"id": "c1", "metric": "error", "operator": "<=", "threshold": 0.5, "unit": "C"}], "results": [{"metric": "error", "value": 0.2, "unit": "C"}]},
}
_NAMES = ["Hypothesis and Crucial-Uncertainty Agent", "Welfare Protocol Design Agent", "Experiment and Analysis Planner", "Multimodal Welfare Analysis Agent", "Statistical and Causal Analysis Agent", "Hardware Concept Agent", "Component and Supply-Chain Agent", "Prototype Evaluation Agent"]
_EXAMPLES["B2"]["sources"] = [{"id": "synthetic-protocol", "passage": "Synthetic protocol: record calibrated sound readings at predefined positions in a synthetic enclosure. No animal welfare validation is claimed.", "context": "synthetic enclosure"}]
_EXAMPLES["B7"]["sources"] = [{"id": "synthetic-catalogue", "passage": "Synthetic supplier record dated 2026-09-01: synthetic-part, 3.3 V, indicative USD 12 and synthetic in-stock status. This is test data, not a real offer.", "context": "synthetic supplier"}]
_REQUIRED = {"B1": {"brief": "object"}, "B2": {"hypothesis": "object", "framework": "object"}, "B3": {"protocol": "object", "resources": "object"}, "B4": {"video": "object"}, "B5": {"rows": "array", "columns": "array", "question": "string"}, "B6": {"requirements": "array"}, "B7": {"requirements": "object", "supplier_records": "array", "as_of": "string"}, "B8": {"criteria": "array", "results": "array"}}
_TASKS = ["Draft falsifiable hypotheses from a structured brief", "Draft a protocol from a user welfare framework", "Plan a comparison and approximate sample requirements", "Annotate bounded synthetic grayscale video frames", "Compute numeric summaries and reproducible analysis", "Map requirements to bench concept components", "Compare approved dated supplier records", "Evaluate bench measurements against predefined thresholds"]
SPECS = {}
for index, agent in enumerate(_REQUIRED):
    SPECS[agent] = {"name": _NAMES[index], "task": _TASKS[index], "required": list(_REQUIRED[agent]),
                    "input_schema": {"type": "object", "required": list(_REQUIRED[agent]), "properties": {k: {"type": v} for k, v in _REQUIRED[agent].items()}},
                    "output_schema": {"type": "object"}, "limitations": ["Deterministic bounded assistance using supplied structured inputs; no independent scientific validation", "Human review required before consequential research decisions"],
                    "modalities": ["synthetic-grayscale-video"] if agent == "B4" else ["structured-json"], "example": dict(_EXAMPLES[agent], data_classification="synthetic"),
                    "baseline": "Simple literal extraction or unadjusted summary; performs no scientific inference"}
SPECS["B4"]["limitations"] += ["2–120 grayscale frames, <=64x64 pixels, <=60 seconds; no audio, compressed-video decoding or welfare diagnosis"]
SPECS["B7"]["limitations"] += ["Exact specification matching only; no live availability or pricing lookup"]
SPECS["B3"]["limitations"] += ["Power approximation is limited to two independent continuous-outcome groups; no clustering adjustment"]
for agent, fields in {
    "B1": {"hypotheses": "array", "theory_of_change": "array", "unresolved_decisions": "array", "belief_forecast": "object"},
    "B2": {"protocol_draft": "object", "unresolved_decisions": "array", "review_needs": "array"},
    "B3": {"design": "string", "sampling": "object", "power_inputs": "object", "analysis_plan": "object", "unresolved_decisions": "array"},
    "B4": {"annotations": "array", "backend": "string", "duration_seconds": "number", "welfare_diagnosis": "null"},
    "B5": {"statistics": "object", "question": "string", "reproducible_script": "string", "causal_assessment": "object"},
    "B6": {"concept_specification": "object", "bench_test_plan": "array", "unresolved_decisions": "array"},
    "B7": {"candidates": "array", "rejected": "array", "as_of": "string"},
    "B8": {"criteria": "array", "recommendation": "string", "deviations": "array", "belief_update": "object"},
}.items():
    SPECS[agent]["output_schema"]["properties"] = {k: {"type": t} for k, t in fields.items()}
for agent, fields in {"B5": {"rows": "object", "columns": "string"}, "B6": {"requirements": "object"}, "B7": {"supplier_records": "object"}, "B8": {"criteria": "object", "results": "object"}}.items():
    for field, kind in fields.items():
        SPECS[agent]["input_schema"]["properties"][field]["items"] = {"type": kind}
SPECS["B4"]["input_schema"]["properties"]["video"]["properties"] = {
    "format": {"type": "string"}, "frames": {"type": "array", "items": {"type": "object", "properties": {
        "timestamp_seconds": {"type": "number"}, "pixels": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}}
    }}}
}
SPECS["B1"]["output_schema"]["properties"]["hypotheses"]["items"] = {
    "type": "object", "properties": {"claim": {"type": "string"}, "test_ready": {"type": "boolean"}, "falsifier": {"type": "string"}}
}
SPECS["B4"]["output_schema"]["properties"]["annotations"]["items"] = {
    "type": "object", "required": ["timestamp_seconds", "mean_brightness", "mean_absolute_pixel_change", "observation", "uncertainty"],
    "properties": {"timestamp_seconds": {"type": "number"}, "mean_brightness": {"type": "number"}, "mean_absolute_pixel_change": {"type": ["number", "null"]},
                   "observation": {"type": "string"}, "uncertainty": {"type": "string"}}
}
SPECS["B7"]["output_schema"]["properties"]["candidates"]["items"] = {
    "type": "object", "required": ["compatibility", "gaps", "conflicts", "freshness", "independent_confirmation_required"],
    "properties": {"compatibility": {"type": "string", "enum": ["conflict", "unknown", "matches_supplied_constraints"]},
                   "gaps": {"type": "array"}, "conflicts": {"type": "array"}, "age_days": {"type": ["integer", "null"]},
                   "freshness": {"type": "string", "enum": ["unknown", "future_timestamp", "stale", "within_requested_age"]},
                   "independent_confirmation_required": {"type": "boolean"}}
}
SPECS["B8"]["output_schema"]["properties"]["criteria"]["items"] = {
    "type": "object", "required": ["criterion_id", "metric", "status", "reason"],
    "properties": {"status": {"type": "string", "enum": ["pass", "fail", "indeterminate"]}, "reason": {"type": "string"}}
}
SPECS["B8"]["output_schema"]["properties"]["recommendation"]["enum"] = ["stop", "revise", "advance"]
_HANDLERS = {f"B{i}": globals()[f"_b{i}"] for i in range(1, 9)}


def run(agent_id, payload):
    missing = [key for key in _REQUIRED[agent_id] if key not in payload]
    if missing:
        return result({}, "abstained", required_action="Provide required fields: " + ", ".join(missing))
    try:
        return _HANDLERS[agent_id](payload)
    except (TypeError, ValueError, KeyError, AttributeError, OverflowError) as exc:
        return result({}, "abstained", ["Malformed structured input: " + type(exc).__name__], "Correct the input structure and finite numeric values; see the supported example.")


def baseline(agent_id, payload):
    """Actual simple computations, intentionally lacking the richer checks."""
    if any(k not in payload for k in _REQUIRED[agent_id]):
        return result({}, "abstained", required_action="Supply required input fields.")
    if agent_id == "B1":
        return result({"hypotheses": [{"claim": str(payload["brief"])}]}, "partial")
    if agent_id == "B2":
        return result({"protocol_draft": {"population": payload["hypothesis"].get("population"), "indicators": payload["framework"].get("indicators", [])}}, "partial")
    if agent_id == "B3":
        n = payload["resources"].get("available_units")
        return result({"sampling": {"approximate_units_per_arm": int(n)//2 if numeric(n) else None}}, "partial")
    if agent_id == "B4":
        frames = payload["video"].get("frames", [])
        return result({"annotations": [{"timestamp_seconds": f.get("timestamp_seconds"), "observation": "frame present"} for f in frames]}, "partial")
    if agent_id == "B5":
        stats = {}
        for col in payload["columns"]:
            values = [r[col] for r in payload["rows"] if numeric(r.get(col))]
            stats[col] = {"n": len(values), "mean": sum(values)/len(values) if values else None}
        return result({"statistics": stats}, "partial")
    if agent_id == "B6":
        return result({"concept_specification": {"components": [{"quantity": r.get("quantity")} for r in payload["requirements"]]}}, "partial")
    if agent_id == "B7":
        return result({"candidates": [dict(r) for r in payload["supplier_records"] if r.get("approved") is True]}, "partial")
    return result({"criteria": [{"criterion_id": c.get("id"), "status": "indeterminate"} for c in payload["criteria"]], "recommendation": "revise"}, "partial")


def benchmark_cases():
    import copy
    cases = []
    def add(agent, category, payload, check):
        cases.append({"id": agent.lower()+"-"+category, "agent_id": agent, "category": category, "input": dict(payload, data_classification="synthetic"), "check": check})
    ordinary = {
        "B1": lambda r: r["data"]["hypotheses"][0]["test_ready"] and "sound level" in r["data"]["hypotheses"][0]["claim"],
        "B2": lambda r: r["status"] == "awaiting_human" and r["data"]["protocol_draft"]["indicators"][0]["source_id"] == "synthetic-protocol",
        "B3": lambda r: r["data"]["sampling"]["approximate_units_per_arm"] == 36,
        "B4": lambda r: r["data"]["annotations"][1]["mean_absolute_pixel_change"] == 10 and r["data"]["welfare_diagnosis"] is None,
        "B5": lambda r: r["data"]["statistics"]["reading"]["mean"] == 2 and r["data"]["statistics"]["reading"]["missing"] == 1,
        "B6": lambda r: r["data"]["concept_specification"]["components"][0]["class"] == "temperature sensor",
        "B7": lambda r: r["data"]["candidates"][0]["compatibility"] == "matches_supplied_constraints" and r["data"]["candidates"][0]["age_days"] == 12,
        "B8": lambda r: r["data"]["criteria"][0]["status"] == "pass" and r["status"] == "awaiting_human",
    }
    for a in _REQUIRED:
        add(a, "ordinary", copy.deepcopy(_EXAMPLES[a]), ordinary[a])
        add(a, "missing", {}, lambda r: r["status"] == "abstained" and bool(r.get("required_action")))
    p = copy.deepcopy(_EXAMPLES["B1"]); p["brief"].pop("comparator")
    add("B1", "adversarial", p, lambda r: not r["data"]["hypotheses"][0]["test_ready"] and "comparator" in r["data"]["unresolved_decisions"])
    add("B1", "task-failure", {"brief": {"intervention": "improve welfare"}}, lambda r: r["status"] == "abstained" and not r["data"]["hypotheses"])
    p = copy.deepcopy(_EXAMPLES["B2"]); p["framework"]["indicators"][0]["validation_population"] = "different species"
    add("B2", "adversarial", p, lambda r: r["data"]["protocol_draft"]["indicators"][0]["validation_status"] == "unverified_context_transfer")
    add("B2", "task-failure", {"hypothesis": {}, "framework": {}}, lambda r: "framework indicators and validation evidence" in r["data"]["unresolved_decisions"])
    p = copy.deepcopy(_EXAMPLES["B3"]); p["protocol"]["clustered"] = True
    add("B3", "adversarial", p, lambda r: r["data"]["sampling"]["approximate_units_per_arm"] is None)
    p = copy.deepcopy(_EXAMPLES["B3"]); p["resources"]["available_units"] = 4
    add("B3", "task-failure", p, lambda r: r["data"]["sampling"]["resource_feasible"] is False)
    p = copy.deepcopy(_EXAMPLES["B4"]); p["video"]["audio"] = "diagnose distress"
    add("B4", "adversarial", p, lambda r: r["status"] == "unsupported_input" and not r["data"]["annotations"])
    p = copy.deepcopy(_EXAMPLES["B4"]); p["video"]["frames"][1]["timestamp_seconds"] = 0
    add("B4", "task-failure", p, lambda r: r["status"] == "abstained")
    p = copy.deepcopy(_EXAMPLES["B5"]); p["question"] = "Prove this intervention causes better welfare"
    add("B5", "adversarial", p, lambda r: r["data"]["causal_assessment"]["causal_effect_estimated"] is False)
    add("B5", "task-failure", {"rows": [{"x": "not numeric"}, {"x": None}], "columns": ["x"], "question": "mean"}, lambda r: r["data"]["statistics"]["x"]["mean"] is None and r["data"]["statistics"]["x"]["invalid"] == 1)
    add("B6", "adversarial", {"requirements": [{"id": "i", "kind": "intervention", "quantity": "temperature"}]}, lambda r: "fail-safe" in r["data"]["concept_specification"]["components"][0]["class"] and r["data"]["bench_test_plan"][0]["animal_use"] is False)
    add("B6", "task-failure", {"requirements": [{"kind": "measurement", "quantity": "happiness"}]}, lambda r: r["status"] == "abstained" and not r["data"]["concept_specification"]["components"])
    p = copy.deepcopy(_EXAMPLES["B7"]); p["supplier_records"][0]["approved"] = False
    add("B7", "adversarial", p, lambda r: not r["data"]["candidates"] and bool(r["data"]["rejected"]))
    p = copy.deepcopy(_EXAMPLES["B7"]); p["supplier_records"][0]["checked_at"] = "2020-01-01"; p["supplier_records"][0]["specifications"] = {}
    add("B7", "task-failure", p, lambda r: r["data"]["candidates"][0]["freshness"] == "stale" and r["data"]["candidates"][0]["compatibility"] == "unknown")
    p = copy.deepcopy(_EXAMPLES["B8"]); p["results"] = []
    add("B8", "adversarial", p, lambda r: r["data"]["criteria"][0]["status"] == "indeterminate" and r["data"]["recommendation"] == "revise")
    p = copy.deepcopy(_EXAMPLES["B8"]); p["criteria"][0]["critical"] = True; p["results"][0]["value"] = 1
    add("B8", "task-failure", p, lambda r: r["data"]["criteria"][0]["status"] == "fail" and r["data"]["recommendation"] == "stop")
    return cases
