import sys
sys.setrecursionlimit(100000)
R,C,M = map(int, input().split())

sharks = [0]
arr = [[0] * (C) for i in range(R)]
for i in range(1, M+1):
    info = list(map(int, input().split()))
    sharks.append(info)
    arr[info[0]-1][info[1]-1] = i


def fishing(v, arr, sharks):
    for i in range(len(arr)):
        if arr[i][v]:
            size = sharks[arr[i][v]][4]
            arr[i][v] = 0
            return size
    else:
        return 0

def moveAll(arr):
    tempArr = [[0] * (len(arr[0])) for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]:
                index = arr[i][j]
                shark = sharks[index]
                x, y, d = move(i, j, shark[2], shark[3])
                sharks[index][3] = d
                if not tempArr[x][y]:
                    tempArr[x][y] = index
                else:
                    if shark[4] > sharks[tempArr[x][y]][4]:
                        tempArr[x][y] = index
    return tempArr

def move(x, y, s, d):
    if s == 0:
        return x, y, d
    # #up
    # if d == 1:
    #     if x == 0:
    #         d = 2
    #         x += 1
    #     else:
    #         x -= 1
    # #down
    # elif d == 2:
    #     if x == R-1:
    #         d = 1
    #         x -= 1
    #     else:
    #         x += 1
    # #right
    # elif d == 3:
    #     if y == C-1:
    #         d = 4
    #         y -= 1
    #     else:
    #         y += 1
    # #left
    # elif d == 4:
    #     if y == 0:
    #         d = 3
    #         y += 1
    #     else:
    #         y -= 1
    #    s -= 1
    # up
    if d == 1:
        if x <= s:
            s -= x
            x = 0
            d = 2
        else:
            x = x-s
            s = 0
    # down
    elif d == 2:
        if R-1-x <= s:
            s -= R-1-x
            x = R-1
            d = 1
        else:
            x = x + s
            s = 0
    #right
    elif d == 3:
        if C - 1 - y <= s:
            s -= C - 1 - y
            y = C - 1
            d = 4
        else:
            y = y + s
            s = 0
    # left
    elif d == 4:
        if y <= s:
            s -= y
            y = 0
            d = 3
        else:
            y = y - s
            s = 0
    return move(x, y, s, d)


result = 0
for i in range(C):
    result += fishing(i, arr, sharks)
    arr = moveAll(arr)
print(result)