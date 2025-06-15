import jsonschema


def validate(data, schema):
    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError:
        return False

    # TODO if $ref or
    if "type" in schema and schema["type"] == "object":
        allowed = list(schema["properties"].keys())
        for key in data.keys():
            if key not in allowed:
                return False

    return True
