import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

# 치킨집과 일반집 위치 구하고, 각 위치에 대해서 치킨거리를 구해야함.
puradak = []
house = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append([i,j])
        elif maps[i][j] == 2:
            puradak.append([i,j])
# 치킨집을 m개 선택했을때 조합
combs = list(combinations(puradak, m))
cand = []

for comb in combs:
    answer = 0
    for h in house:
        x1, y1 = h
        dist = int(1e9)
        for c in comb:
            x2, y2 = c
            dist = min(dist, abs(x1-x2) + abs(y1-y2))
        answer+=dist
    cand.append(answer)
print(min(cand))
