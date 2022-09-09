import sys

N, M = map(int, input().split())
listA = []
result =[]
blackList = []
whiteList = []
for i in range(8):
    tempListA = []
    tempListB = []
    for j in range(8):
        color1 = 'W'
        color2 = 'B'
        if (i + j) % 2 == 0:
            color1 = 'B'
            color2 = 'W'
        tempListA.append(color1)
        tempListB.append(color2)
    blackList.append(tempListA)
    whiteList.append(tempListB)

for _ in range(N):
    listA.append(list(sys.stdin.readline().strip()))

for i in range(N-8+1):
    for j in range(M-8+1):
        cntA = 0
        cntB = 0
        for k in range(8):
            for t in range(8):
                if listA[i+k][j+t] != blackList[k][t]:
                    cntA += 1
                if listA[i+k][j+t] != whiteList[k][t]:
                    cntB += 1

        result.append(cntA)
        result.append(cntB)

print(result, min(result))