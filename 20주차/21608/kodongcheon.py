import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N**2):
    arr.append(list(map(int, input().split())))

classRoom = [[0]*(N+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(N+2):
        if i == 0 or j == 0 or i == N+1 or j == N+1:
            classRoom[i][j] = 10000

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for student in arr:
    nullCnt = 0
    likeCnt = 0
    x, y = 0, 0
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            likeTemp = 0
            nullTemp = 0
            if classRoom[i][j] != 0:
                continue
            for dx, dy in move:
                studentNum = classRoom[i+dx][j+dy]
                if studentNum in student:
                    likeTemp += 1
                elif studentNum == 0:
                    nullTemp +=1
            if likeTemp > likeCnt:
                likeCnt = likeTemp
                nullCnt = nullTemp
                x, y = i, j
            elif likeTemp == likeCnt and nullTemp > nullCnt:
                nullCnt = nullTemp
                x, y = i ,j
            elif likeTemp == likeCnt and nullTemp == nullCnt:
                x, y = i, j
    classRoom[x][y] = student[0]

result = 0
for student in arr:
    for i in range(1, N+1):
        for j in range(1, N+1):
            if classRoom[i][j] == student[0]:
                cnt = 0
                for dx, dy in move:
                    studentNum = classRoom[i + dx][j + dy]
                    if studentNum in student:
                        cnt += 1
                if cnt == 0:
                    result += 0
                elif cnt == 1:
                    result += 1
                elif cnt == 2:
                    result += 10
                elif cnt == 3:
                    result += 100
                else:
                    result += 1000

print(result)






