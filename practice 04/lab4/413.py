import json
import re

def resolve_query(data, query):
    try:
        # Split by dots but keep array indices
        parts = re.split(r'\.(?![^\[]*\])', query)

        current = data

        for part in parts:
            # Extract key and indices like friends[2][1]
            matches = re.finditer(r'([^\[\]]+)|\[(\d+)\]', part)
            for match in matches:
                key, index = match.groups()

                if key is not None:
                    if not isinstance(current, dict) or key not in current:
                        return "NOT_FOUND"
                    current = current[key]

                elif index is not None:
                    index = int(index)
                    if not isinstance(current, list) or index >= len(current):
                        return "NOT_FOUND"
                    current = current[index]

        return json.dumps(current, separators=(',', ':'))

    except:
        return "NOT_FOUND"


# Input
data = json.loads(input())
q = int(input())

for _ in range(q):
    query = input().strip()
    result = resolve_query(data, query)
    print(result)