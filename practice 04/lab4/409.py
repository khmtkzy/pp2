def powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i


# Input
n = int(input())

# Output
for num in powers_of_two(n):
    print(num, end=" ")