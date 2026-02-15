a = int(input())
b = list(map(int,input().split()))
cnt = 0
for i in b:
    if i > 0:
        cnt += 1
print(cnt)