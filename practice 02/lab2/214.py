a = int(input())
b = list(map(int, input().split()))
mx = 0
ans = b[0]
for x in b:
    count = b.count(x)
    if count > mx:
        mx = count
        ans = x
    elif count == mx and x < ans:
        ans = x
print(ans)