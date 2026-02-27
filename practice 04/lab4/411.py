import json

def apply_patch(source, patch):
    for key, value in patch.items():
        if value is None:
            # Remove key if exists
            source.pop(key, None)
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            # Recursive patch if both are dictionaries
            apply_patch(source[key], value)
        else:
            # Add or replace
            source[key] = value
    return source


# Input
source = json.loads(input())
patch = json.loads(input())

# Apply patch
result = apply_patch(source, patch)

# Output (compact + sorted keys)
print(json.dumps(result, separators=(',', ':'), sort_keys=True))