from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int,input().split())) for i in range(N)]
arr2 = []
arr1 = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            arr2.append((i,j))
        elif arr[i][j] == 1:
            arr1.append((i,j))

temp = list(combinations(arr2, M))
mindistance = 1000000
for i in range(len(temp)):
    result = 0
    for xi, yi in arr1:
        dist = 10000
        for x, y in temp[i]:
            dist = min(dist,abs(xi-x)+abs(yi-y))
        result += dist
    mindistance = min(mindistance, result)
print(mindistance)