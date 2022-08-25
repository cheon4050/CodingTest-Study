import sys

n = int(sys.stdin.readline())
eggs = []
for i in range(n):
    durability, weight = map(int, sys.stdin.readline().split())
    eggs.append([durability, weight])

result = 0
def dfs(position: int, count: int) -> None:
    if position == n:
        global result
        result = max(result, count)
        return
    egg_check = False
    for i in range(n):
        if i != position and eggs[position][0] > 0 and eggs[i][0] > 0:
            if not egg_check:
                egg_check = True
            break_egg = 0
            eggs[i][0] -= eggs[position][1]
            eggs[position][0] -= eggs[i][1]
            if eggs[i][0] <= 0:
                break_egg += 1
            if eggs[position][0] <= 0:
                break_egg += 1
            dfs(position + 1, count + break_egg)
            eggs[i][0] += eggs[position][1]
            eggs[position][0] += eggs[i][1]
    if not egg_check:
        dfs(position + 1, count)

dfs(0, 0)
print(result)