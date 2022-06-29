# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
#
# arr=[]
# for _ in range(N):
#     temp = list(map(int, input().split()))
#     arr.append(temp)
# tetromino = [[(0,0),(0,1),(0,2),(0,3)], [(0,0),(1,0),(2,0),(3,0)], [(0,0),(0,1),(1,0),(1,1)],
#              [(0,0),(1,0),(2,0),(2,1)], [(0,0),(1,0),(0,1),(0,2)], [(0,0),(0,1),(1,1),(2,1)],[(1,0),(1,1),(1,2),(0,2)],
#              [(2,0),(2,1),(1,1),(0,1)], [(0,0),(1,0),(1,1),(2,1)], [(0,0),(1,0),(2,0),(0,1)],[(0,0),(0,1),(0,2),(1,2)],
#              [(0,0),(1,0),(1,1),(2,1)], [(1,0),(1,1),(0,1),(0,2)], [(0,0),(0,1),(1,1),(1,2)],[(1,0),(2,0),(1,1),(0,1)],
#              [(0,0),(0,1),(0,2),(1,1)], [(1,0),(1,1),(0,1),(2,1)], [(1,0),(1,1),(1,2),(0,1)],[(0,0),(1,0),(2,0),(1,1)]]
# result = 0
# for tetro in tetromino:
#     for i in range(N):
#         for j in range(M):
#             x1, y1 = i+tetro[0][0] , j+tetro[0][1]
#             x2, y2 = i+tetro[1][0] , j+tetro[1][1]
#             x3, y3 = i+tetro[2][0] , j+tetro[2][1]
#             x4, y4 = i+tetro[3][0] , j+tetro[3][1]
#             if 0 <= x1 <N and 0 <= y1 <M and 0 <= x2 <N and 0 <= y2 <M and 0 <= x3 <N and 0 <= y3 <M and 0 <= x4 <N and 0 <= y4 <M:
#                 result = max(result, arr[x1][y1]+arr[x2][y2]+arr[x3][y3]+arr[x4][y4])
#
# print(result)

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr=[]
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

result = 0
def dfs(arr,x, y, i, j, cnt, total):
    global result
    if not 0<=i<len(arr) or not 0<=j<len(arr[0]):
        return
    if cnt == 3:
        result = max(result, total+arr[i][j])
    else:
        if not(x == i-1 and y == j):
            dfs(arr, i, j, i - 1, j, cnt + 1, total + arr[i][j])
        if not(x == i+1 and y == j):
            dfs(arr, i, j, i + 1, j, cnt + 1, total + arr[i][j])
        if not(x == i and y == j-1):
            dfs(arr, i, j, i, j - 1, cnt + 1, total + arr[i][j])
        if not(x == i and y == j+1):
            dfs(arr, i, j, i, j + 1, cnt + 1, total + arr[i][j])

for i in range(N):
    for j in range(M):
        dfs(arr,i, j, i,j,0,0)
tetromino =[(0,0),(0,1),(0,2),(1,1)], [(1,0),(1,1),(0,1),(2,1)], [(1,0),(1,1),(1,2),(0,1)],[(0,0),(1,0),(2,0),(1,1)]
for tetro in tetromino:
    for i in range(N):
        for j in range(M):
            x1, y1 = i+tetro[0][0] , j+tetro[0][1]
            x2, y2 = i+tetro[1][0] , j+tetro[1][1]
            x3, y3 = i+tetro[2][0] , j+tetro[2][1]
            x4, y4 = i+tetro[3][0] , j+tetro[3][1]
            if 0 <= x1 <N and 0 <= y1 <M and 0 <= x2 <N and 0 <= y2 <M and 0 <= x3 <N and 0 <= y3 <M and 0 <= x4 <N and 0 <= y4 <M:
                result = max(result, arr[x1][y1]+arr[x2][y2]+arr[x3][y3]+arr[x4][y4])
print(result)
