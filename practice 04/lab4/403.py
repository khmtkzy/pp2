a = int(input())
b = []
for i in range(0, a+1):
    if i % 3 == 0 and i % 4 == 0:
        b.append(i)
print(*b)

def divisible_numbers(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Input
n = int(input())

# Output
for number in divisible_numbers(n):
    print(number, end=" ")