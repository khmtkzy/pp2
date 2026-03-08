n = int(input())
nums = list(map(int, input().split()))

unique_sorted = sorted(set(nums))

print(*unique_sorted)