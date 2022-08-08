N = int(input())

arr = [[False] * 367 for i in range(N+1)]
temp = []
for T in range(N):
    S, E = map(int,input().split())
    temp.append((S,E))
temp.sort(key= lambda x : (x[0],-x[1]+x[0]))

for S, E in temp:
    for i in range(N):
        for j in range(S, E+1):
            if arr[i][j] == True:
                break
        else:
            for j in range(S, E+1):
                arr[i][j] = True
            break
result = 0
start = 1
for j in range(1,367):
    for i in range(N):
        if arr[i][j] == True:
            break
    else:
        for x in range(N+1):
            if sum(arr[x][start:j]) == 0:
                result += (j-start) * x
                break
        start = j + 1
print(result)

