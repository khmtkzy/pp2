import re

text = "ab abb abbb abbbb"
pattern = r"ab{2,3}"

print(re.findall(pattern, text))