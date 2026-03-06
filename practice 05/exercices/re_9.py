import re

text = "HelloWorldPythonRegex"

result = re.sub(r"(?<!^)([A-Z])", r" \1", text)

print(result)