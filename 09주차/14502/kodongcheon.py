from collections import deque
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
print(arr)
def bfs(v, visited,arr):
    queue = deque()
    queue.append(v)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while(queue):
        x, y =queue.popleft()
        visited[x][y] = True
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if not(0<= temp_x <N and 0 <= temp_y < M):
                continue
            if arr[temp_x][temp_y] == 1 or arr[temp_x][temp_y] == 2:
                continue
            else:
                arr[temp_x][temp_y] = 2
                queue.append((temp_x,temp_y))

visited = [[False]*M for _ in range(N)]
result = 0
for x1 in range(N):
    for y1 in range(M):
        for x2 in range(N):
            for y2 in range(M):
                for x3 in range(N):
                    for y3 in range(M):
                        arr2 = arr
                        arr2[x1][y1] = 1
                        arr2[x2][y2] = 1
                        arr2[x3][y3] = 1
                        print(arr2)
                        for i in range(N):
                            for j in range(M):
                                if not visited[i][j] and arr2[i][j] == 2:
                                    bfs((i,j),visited,arr2)
                                    num = 0
                                    for k in range(len(arr2)):
                                        for t in range(len(arr2)):
                                            if arr2[k][t] == 0:
                                                num +=1
                                    result = max(num, result)


print(result)
