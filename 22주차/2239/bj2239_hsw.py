import sys

board = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(9)]
row = [[False for _ in range(10)] for _ in range(9)]
column = [[False for _ in range(10)] for _ in range(9)]
square = [[False for _ in range(10)] for _ in range(9)]
missing = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            missing.append((i, j))
        else:
            row[i][board[i][j]] = column[j][board[i][j]] = square[(i // 3) * 3 + (j // 3)][board[i][j]] = True

def solve(start: int) -> None:
    if start == len(missing):
        for line in board:
            print(''.join(map(str, line)))
        sys.exit(0)
    r, c = missing[start]
    for num in range(1, 10):
        if not row[r][num] and not column[c][num] and not square[(r // 3) * 3 + (c // 3)][num]:
            row[r][num] = column[c][num] = square[(r // 3) * 3 + (c // 3)][num] = True
            board[r][c] = num
            solve(start + 1)
            row[r][num] = column[c][num] = square[(r // 3) * 3 + (c // 3)][num] = False
            board[r][c] = 0
solve(0)