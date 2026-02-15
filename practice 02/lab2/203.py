a = int(input())
b = list(map(int,input().split()))
sum = 0
for i in b:
    sum = sum + i
print(sum)

#print(sum(b))