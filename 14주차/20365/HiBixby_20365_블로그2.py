n = int(input())
colors = input()
d = {"B": 0, "R": 0}

for i, color in enumerate(colors):
    if colors[i-1] != color:
        d[color] += 1
print(min(d["R"], d["B"])+1)
