from functools import reduce
a = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, a))