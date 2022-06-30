ans = int(1e9)
N, M = map(int, input().split())
A, B, b = [], [], []

for r in range(N):
    row = list(map(int, input().split()))
    for c, x in enumerate(row):
        if x == 1:
            A.append((r, c))
        elif x == 2:
            B.append((r, c))
lenB = len(B)

def f(i, m):
    global ans, b
    if i == lenB:
        if m == M:
            ans = min(ans, sum([min([abs(ar-br)+abs(ac-bc) for br, bc in b]) for ar, ac in A]))
        return
    b.append(B[i])
    f(i+1, m+1)
    b.pop()
    f(i+1, m)

f(0, 0)
print(ans)