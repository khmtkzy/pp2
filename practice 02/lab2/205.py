a = int(input())
while a > 1:
    if a % 2 != 0:
        print("NO")
        break
    a = a // 2
else:
    print("YES")

n = int(input())

while n % 2 == 0:
    n = n // 2

if n == 1:
    print("YES")
else:
    print("NO")