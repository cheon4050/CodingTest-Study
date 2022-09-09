n,m = map(int, input().split())
board=[input() for _ in range (n)]
paint = []

for i in range(n-7):
    for j in range(m-7):
        start_W = 0
        start_B = 0
        for x in range(i, i+8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        start_W += 1
                    if board[x][y] != 'B':
                        start_B += 1
                else:
                    if board[x][y] != 'B':
                        start_W += 1
                    if board[x][y] != 'W':
                        start_B += 1
        paint.append(start_W)
        paint.append(start_B)
print(min(paint))