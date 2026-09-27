"""Small, explicit JSON Schema subset used by the versioned manifests.

Manifests use only the subset implemented below; this is not a complete JSON
Schema engine. Metadata keywords are descriptive and ignored.
"""
import math

class ValidationError(ValueError):
    pass


def validate(value, schema, path='$'):
    kind = schema.get('type')
    types = {'object': dict, 'array': list, 'string': str, 'boolean': bool,
             'number': (int, float), 'integer': int, 'null': type(None)}
    if isinstance(kind, list):
        for option in kind:
            try:
                validate(value, {**schema, 'type': option}, path)
                return
            except ValidationError:
                pass
        raise ValidationError(path + ': invalid type')
    if kind:
        if kind not in types:
            raise ValidationError(path + ': unsupported schema type')
        if not isinstance(value, types[kind]) or (kind in ('number', 'integer') and isinstance(value, bool)):
            raise ValidationError(path + ': expected ' + kind)
    if isinstance(value, float) and not math.isfinite(value):
        raise ValidationError(path + ': non-finite numbers are unsupported')
    if 'enum' in schema and value not in schema['enum']:
        raise ValidationError(path + ': value outside enum')
    if isinstance(value, dict):
        missing = set(schema.get('required', [])) - value.keys()
        if missing:
            raise ValidationError(path + ': supply ' + ', '.join(sorted(missing)))
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False and set(value) - props.keys():
            raise ValidationError(path + ': unknown properties')
        for key, item in value.items():
            validate(item, props.get(key, {}), path + '.' + key)
    elif isinstance(value, list):
        if len(value) < schema.get('minItems', 0) or len(value) > schema.get('maxItems', float('inf')):
            raise ValidationError(path + ': invalid item count')
        for i, item in enumerate(value):
            validate(item, schema.get('items', {}), path + '[' + str(i) + ']')
    elif isinstance(value, str):
        if len(value) < schema.get('minLength', 0) or len(value) > schema.get('maxLength', float('inf')):
            raise ValidationError(path + ': invalid text length')
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema.get('minimum', -float('inf')) or value > schema.get('maximum', float('inf')):
            raise ValidationError(path + ': value outside range')
