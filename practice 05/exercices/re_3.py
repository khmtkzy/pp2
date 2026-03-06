import re

text = "hello_world test_case goodDay"
pattern = r"[a-z]+_[a-z]+"

print(re.findall(pattern, text))