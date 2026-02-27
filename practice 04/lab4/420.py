import sys

k = int(sys.stdin.readline())

g = 0
n = 0

for _ in range(k):
    scope, value = sys.stdin.readline().split()
    value = int(value)
    
    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
    # "local" does nothing

print(g, n)