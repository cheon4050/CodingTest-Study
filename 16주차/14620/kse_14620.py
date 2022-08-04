from itertools import combinations

N = int(input())
F = [[*map(int, input().split())] for _ in range(N)]
ds = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
v = {1, 2, N, N + 1, N - 1, 2 * N}
I = []
P = {}

def ck(a, b, c):
    if abs(a - b) in v or abs(b - c) in v or abs(c - a) in v:
        return False
    return True

for x in range(1, N - 1):
    for y in range(1, N - 1):
        res = 0
        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            res += F[nx][ny]

        i = N * x + y
        P[i] = res
        I.append(i)

ans = min(sum(P[f] for f in flowers) for flowers in combinations(I, 3) if ck(*flowers))
print(ans)