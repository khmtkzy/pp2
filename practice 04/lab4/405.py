def generator(a):
    for i in range(a, 0-1, -1):
        yield i
a = int(input())
for i in generator(a):
    print(i)