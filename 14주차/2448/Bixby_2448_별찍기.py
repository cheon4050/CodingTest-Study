n = int(input())
li = [[' ' for _ in range(2 * n)] for _ in range(n)]
dx = (0, -1, 1, 2, 1, 0, -1, -2)
dy = (0, 1, 1, 2, 2, 2, 2, 2)


def star(size, x, y):
    if size == 3:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            li[ny][nx] = '*'
    else:
        newSize = size // 2
        star(newSize, x, y)
        star(newSize, x - newSize, y + newSize)
        star(newSize, x + newSize, y + newSize)


star(n, n - 1, 0)
for i in li:
    print(''.join(i))
