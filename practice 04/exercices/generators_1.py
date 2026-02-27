def square_generator(N):
    for i in range(N + 1):
        yield i * i

# Example usage
N = 5
for value in square_generator(N):
    print(value)