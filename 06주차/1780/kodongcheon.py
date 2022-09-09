import sys
input = sys.stdin.readline

def CHECK(k,a, b,visited,result,arr):
    if k == 1:
        if visited[a][b] == False:
            result[arr[a][b]+1] += 1
        return
    for i in range(a, a+k):
        for j in range(b, b+k):
            if visited[i][j] == True or arr[a][b] != arr[i][j]:
                return
    for i in range(a, a + k):
        for j in range(b, b + k):
            visited[i][j] = True
    result[arr[a][b]+1] +=1
N = int(input())
arr = []
visited = [[False] * N for i in range(N)]
result = [0]*3

for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

for k in range(7,-1,-1):
    for i in range(0,N-3**k+1,3**k):
        for j in range(0,N-3**k+1,3**k):
            if visited[i][j] != True:
                CHECK(3**k, i, j, visited, result,arr)
for count in result:
    print(count)