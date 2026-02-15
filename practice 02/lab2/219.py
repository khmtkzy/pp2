n = int(input())
dramas = {}
for _ in range(n):
    name, episodes = input().split()
    episodes = int(episodes)

    if name in dramas:
        dramas[name] += episodes
    else:
        dramas[name] = episodes
for name in sorted(dramas):
    print(name, dramas[name])