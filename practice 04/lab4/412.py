import json

def deep_diff(obj1, obj2, path=""):
    differences = []

    keys = set(obj1.keys()) | set(obj2.keys())

    for key in keys:
        new_path = f"{path}.{key}" if path else key

        if key not in obj1:
            differences.append(
                f"{new_path} : <missing> -> {json.dumps(obj2[key], separators=(',', ':'))}"
            )
        elif key not in obj2:
            differences.append(
                f"{new_path} : {json.dumps(obj1[key], separators=(',', ':'))} -> <missing>"
            )
        else:
            val1 = obj1[key]
            val2 = obj2[key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                differences.extend(deep_diff(val1, val2, new_path))
            elif val1 != val2:
                differences.append(
                    f"{new_path} : {json.dumps(val1, separators=(',', ':'))} -> {json.dumps(val2, separators=(',', ':'))}"
                )

    return differences


# Input
obj1 = json.loads(input())
obj2 = json.loads(input())

# Compute differences
diffs = deep_diff(obj1, obj2)

# Output
if not diffs:
    print("No differences")
else:
    for line in sorted(diffs):
        print(line)