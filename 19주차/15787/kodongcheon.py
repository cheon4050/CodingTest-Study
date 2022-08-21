import sys
input = sys.stdin.readline
N, M = map(int, input().split())

trainList = [[0]*20 for i in range(N+1)]

for _ in range(M):
    commands = list(map(int, input().split()))
    if commands[0] == 1:
        trainList[commands[1]][commands[2]-1] = 1
    elif commands[0] == 2:
        trainList[commands[1]][commands[2]-1] = 0
    elif commands[0] == 3:
        trainList[commands[1]].pop()
        trainList[commands[1]] = [0]+trainList[commands[1]]
    else:
        trainList[commands[1]].pop(0)
        trainList[commands[1]].append(0)
result = []
for i in range(1,N+1):
    if not trainList[i] in result:
        result.append(trainList[i])
print(len(result))