import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = []
temp =[]
for i in range(R):
    arr.append(list(map(int,input().split())))
    if arr[i][0] == -1:
        temp.append(i)

def bfs(arr):
    visited = [[0] * (len(arr[0])) for _ in range(len(arr))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                for k in range(4):
                    x = dx[k] + i
                    y = dy[k] + j
                    if 0 <= x < len(arr) and 0<= y < len(arr[0]):
                        if arr[x][y] == -1:
                            continue
                        visited[x][y] +=arr[i][j]//5
                        cnt += arr[i][j]//5
                arr[i][j] -= cnt
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] +=visited[i][j]

def Cycle_top(arr, x):
    for i in range(x-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for i in range(1,len(arr[0])):
        arr[0][i-1] = arr[0][i]
    for i in range(x):
        arr[i][-1] = arr[i+1][-1]
    for i in range(len(arr[0])-1, 0, -1):
        arr[x][i] = arr[x][i-1]
    arr[x][1] = 0

def Cycle_bottom(arr,x):
    for i in range(x+1, len(arr)-1):
        arr[i][0] = arr[i+1][0]
    for i in range(1,len(arr[0])):
        arr[-1][i-1] = arr[-1][i]
    for i in range(len(arr)-1, x-1, -1):
        arr[i][-1] = arr[i-1][-1]
    for i in range(len(arr[0])-1, 0, -1):
        arr[x][i] = arr[x][i-1]
    arr[x][1] = 0

for _ in range(T):
    bfs(arr)
    Cycle_top(arr, temp[0])
    Cycle_bottom(arr, temp[1])

result = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        result += arr[i][j]
print(result+2)