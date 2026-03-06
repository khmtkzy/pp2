import re

text = "HelloWorldPythonRegex"

result = re.split(r"(?=[A-Z])", text)

print(result)