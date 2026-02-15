a, l, r =map(int, input().split())
b = list(map(int, input().split()))
l -= 1
r -= 1
while l < r:
    b[l], b[r] = b[r], b[l]
    l += 1
    r -= 1
print(*b)