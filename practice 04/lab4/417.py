import sys
import math

# Read input
R = float(sys.stdin.readline())
x1, y1 = map(float, sys.stdin.readline().split())
x2, y2 = map(float, sys.stdin.readline().split())

dx = x2 - x1
dy = y2 - y1

# Quadratic coefficients
a = dx*dx + dy*dy
b = 2 * (x1*dx + y1*dy)
c = x1*x1 + y1*y1 - R*R

# Discriminant
D = b*b - 4*a*c

# Total segment length
segment_length = math.sqrt(a)

if D < 0:
    # No intersection
    # Check if entire segment inside
    if x1*x1 + y1*y1 <= R*R and x2*x2 + y2*y2 <= R*R:
        print(f"{segment_length:.10f}")
    else:
        print("0.0000000000")
else:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2*a)
    t2 = (-b + sqrtD) / (2*a)
    
    left = max(0.0, min(t1, t2))
    right = min(1.0, max(t1, t2))
    
    if left > right:
        print("0.0000000000")
    else:
        inside_fraction = right - left
        print(f"{inside_fraction * segment_length:.10f}")