import re

text = "Hello World Test python"
pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, text))