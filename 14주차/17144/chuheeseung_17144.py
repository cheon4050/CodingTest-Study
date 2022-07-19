import copy

r, c, t = map(int, input().split())
graph = []
condi = []

for _ in range(r):
    graph.append(list(map(int, input().split())))

for i in range(r):
    if graph[i][0] == -1:
        condi.append(i)

temp = [[0] * c for _ in range(r)] # 각 구역에서 확산이 일어난 후의 상황을 배열에 저장

def bfs(x, y):
    dust = 0
    count = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    if graph[x][y] != 0 and graph[x][y] != -1:
        dust = graph[x][y] // 5

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != -1:
                    count += 1
                    temp[nx][ny] += dust

        temp[x][y] += graph[x][y] - dust * count

        for i in condi:
            temp[i][0] = -1

    return temp

a = condi[0] # 공기청정기의 위치를 변수에 저장
b = condi[1]

def air(graph, new_graph):
    # new_graph : 초기 그래프에서 미세먼지가 확산된 상황
    # new_graph에서 공기청정기가 작동된 이후의 상황을 graph에 반영
    # graph는 초기 상태와 다르게 공기청정기가 작동된 이후의 상황으로 바뀜

    for i in range(0, len(graph[a]) - 1):
        graph[a][i+1] = new_graph[a][i]
        if new_graph[a][i] == -1:
            graph[a][i+1] = 0

    for i in range(1, len(graph[0])):
        graph[0][i-1] = new_graph[0][i]

    for i in range(0, a-1):
        graph[i+1][0] = new_graph[i][0]

    for i in range(0, a):
        graph[i][c-1] = new_graph[i+1][c-1]

    for i in range(1, a):
        for j in range(1, c-1):
            graph[i][j] = new_graph[i][j]

    for i in range(0, len(graph[b])-1):
        graph[b][i+1] = new_graph[b][i]
        if new_graph[b][i] == -1:
            graph[b][i+1] = 0

    for i in range(1, len(graph[r-1])):
        graph[r-1][i-1] = new_graph[r-1][i]

    for i in range(b+1, r-1):
        graph[i][0] = new_graph[i+1][0]

    for i in range(b, r-1):
        graph[i+1][c-1] = new_graph[i][c-1]

    for i in range(b+1, r-1):
        for j in range(1, c-1):
            graph[i][j] = new_graph[i][j]

    for i in condi:
        graph[i][0] = -1


while t != 0: # 1초마다 미세먼지 확산, 공기청정기 작동해야 함
    for i in range(r):
        for j in range(c):
            # new_graph : 미세먼지가 확산된 이후의 상황
            new_graph = bfs(i, j)

    air(graph, new_graph) # air()를 통해서 공기청정기가 작동된 이후의 상황을 new_graph에 저장
    temp = [[0] * c for _ in range(r)] # 매초마다 새로운 확산이 발생 -> temp 배열 초기화
    t -= 1

result = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] != -1:
            result += graph[i][j]

print(result)