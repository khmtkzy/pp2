def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Input
n = int(input())

# Output
print(",".join(str(num) for num in fibonacci(n)))