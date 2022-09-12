import sys
input = sys.stdin.readline

R, C = map(int,input().split())

arr = []
for i in range(R):
    arr.append(input().rstrip())

moves = [(-1,0), (1, 0), (0, -1), (0, 1)]
newMap = [['.']*C for i in range(R)]
minX = 100
maxX = 0
minY = 100
maxY = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            cnt = 0
            for move in moves:
                if 0<=i+move[0]<R and 0<=j+move[1] < C and  arr[i+move[0]][j + move[1]] == 'X':
                    cnt +=1
            if cnt >= 2:
                newMap[i][j] = 'X'
                minX = min(minX, i)
                minY = min(minY, j)
                maxX = max(maxX, i)
                maxY = max(maxY, j)
for i in range(minX, maxX+1):
    for j in range(minY, maxY+1):
        print(newMap[i][j], end= "")
    print()