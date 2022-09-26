def check(arr, x, y):
    color = arr[x][y]
    # 오른쪽
    for i in range(1, 5):
        if not (y + i < 19 and arr[x][y + i] == color):
            break
    else:
        if (y + 5 == 19 or arr[x][y + 5] != color) and (y-1 == -1 or arr[x][y-1] !=color):
            return True
    # 아래
    for i in range(1, 5):
        if not (x + i < 19 and arr[x + i][y] == color):
            break
    else:
        if (x + 5 == 19 or arr[x + 5][y] != color) and (x - 1 == -1 or arr[x-1][y] != color):
            return True

    # 위 대각선
    for i in range(1, 5):
        if not (0 <= x - i and y + i < 19 and arr[x - i][y + i] == color):
            break
    else:
        if (-1 == x - 5 or y + 5 == 19 or arr[x - 5][y + 5] != color) and (x+1 == 19 or y-1 == -1 or arr[x+1][y-1] != color):
            return True

    # 아래 대각선
    for i in range(1, 5):
        if not (x + i < 19 and y + i < 19 and arr[x + i][y + i] == color):
            break
    else:
        if (x + 5 == 19 or y + 5 == 19 or arr[x + 5][y + 5] != color) and (x-1 == -1 or y-1 == -1 or arr[x-1][y-1] != color):
            return True
    return False

arr = [list(map(int, input().split()))for i in range(19)]

x, y, flag = 0, 0, False
for j in range(19):
    for i in range(19):
        if arr[i][j] != 0:
            if check(arr,i,j):
                x, y, flag = i, j, True

if flag:
    print(arr[x][y])
    print(x + 1, y + 1)
else:
    print(0)