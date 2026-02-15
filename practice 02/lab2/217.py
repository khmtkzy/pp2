a = int(input())
contacts = {}
for _ in range(a):
    num = input()
    if num in contacts:
        contacts[num] += 1
    else:
        contacts[num] = 1
count = 0
for key in contacts:
    if contacts[key] == 3:
        count += 1
print(count)