import re

s = input()

def double_digit(m):
    return m.group() * 2

result = re.sub(r'\d', double_digit, s)
print(result)