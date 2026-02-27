import sys
import math

R = float(sys.stdin.readline())
x1, y1 = map(float, sys.stdin.readline().split())
x2, y2 = map(float, sys.stdin.readline().split())

# Distance between A and B
dist_AB = math.hypot(x2 - x1, y2 - y1)

# Function to check if segment intersects circle interior
def intersects():
    # Projection method
    dx = x2 - x1
    dy = y2 - y1
    
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - R*R
    
    D = b*b - 4*a*c
    if D < 0:
        return False
    
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2*a)
    t2 = (-b + sqrtD) / (2*a)
    
    # If any intersection point lies strictly inside segment
    return (0 < t1 < 1) or (0 < t2 < 1)

if not intersects():
    print(f"{dist_AB:.10f}")
else:
    dA = math.hypot(x1, y1)
    dB = math.hypot(x2, y2)
    
    # Tangent lengths
    tA = math.sqrt(dA*dA - R*R)
    tB = math.sqrt(dB*dB - R*R)
    
    # Angle between OA and OB
    dot = x1*x2 + y1*y2
    theta = math.acos(dot / (dA*dB))
    
    alpha = math.acos(R / dA)
    beta = math.acos(R / dB)
    
    arc_angle = theta - alpha - beta
    arc_length = R * arc_angle
    
    result = tA + tB + arc_length
    print(f"{result:.10f}")