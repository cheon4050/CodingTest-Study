import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []

for i in range(n): # 치킨집과 일반집 위치를 배열에 저장
    for j in range(n):
        if maps[i][j] == 1:
            house.append([i, j])
        elif maps[i][j] == 2:
            chicken.append([i, j])

combs = list(combinations(chicken, m)) # 치킨집을 m개 선택했을 때 조합
distances = []

for comb in combs:
    answer = 0

    for h in house:
        x1, y1 = h
        dist = int(1e9)

        for c in comb:
            x2, y2 = c
            dist = min(dist, abs(x1 - x2) + abs(y1 - y2)) # 일반집과 치킨집 사이의 최단 거리를 구하기
        answer += dist
    distances.append(answer)

print(min(distances)) # 조합에서 구한 치킨 거리 중 가장 작은 치킨 거리 출력