import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split()) # n : 지역의 개수, m : 수색 범위, r : 길의 개수
item = [-1] + list(map(int, input().split())) # 각 구역 아이템의 수
distance = [[INF for i in range(n + 1)] for j in range(n + 1)]
result = 0

for i in range(1, n + 1): # distance 리스트 자기 자신은 0으로 변경
    distance[i][i] = 0

for i in range(r): # 입력 받아서 distance 리스트에 값을 넣음
    a, b, l = map(int, input().split()) # a, b : 양 끝 지역 번호, l : 길의 길이

    distance[a][b] = l
    distance[b][a] = l

for i in range(1, n + 1): # 플로이드-와샬 알고리즘
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if distance[j][k] > distance[j][i] + distance[i][k]:
                distance[j][k] = distance[j][i] + distance[i][k]

for i in range(1, n + 1):
    temp = 0

    for j in range(1, n + 1):  
        if distance[i][j] <= m: # 수색범위보다 안에 있으면 temp에 추가
            temp += item[j]

    if temp> result:
        result += temp

print(result)