import re

text = "aab acb a123b axxb ab"
pattern = r"a.*b"

print(re.findall(pattern, text))