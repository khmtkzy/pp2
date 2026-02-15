a = int(input())
sol = {}
for i in range(a):
    soz = input()
    if soz not in sol:
        sol[soz] = i + 1
for key in sorted(sol):
    print(key, sol[key])