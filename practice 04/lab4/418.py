import sys

x1, y1 = map(float, sys.stdin.readline().split())
x2, y2 = map(float, sys.stdin.readline().split())

# Parameter t
t = y1 / (y1 + y2)

# Reflection x-coordinate
x = x1 + t * (x2 - x1)

print(f"{x:.10f} 0.0000000000")