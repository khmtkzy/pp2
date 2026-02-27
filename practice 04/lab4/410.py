def limited_cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item


# Input
lst = input().split()
n = int(input())

# Output
for element in limited_cycle(lst, n):
    print(element, end=" ")