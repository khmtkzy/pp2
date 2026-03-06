import re

text = "abbb a ab abb ac"
pattern = r"ab*"

print(re.findall(pattern, text))