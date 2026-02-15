a = int(input())
b = list(map(int, input().split()))
mx = b[0]
mn = b[0]
for i in range(a):
    if mx < b[i]:
        mx = b[i]
    if mn > b[i]:
        mn = b[i]
for i in range(a):
    if b[i] == mx:
        b[i] = mn
print(*b)