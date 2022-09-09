N, r, c = map(int, input().split())

def Z_Search(n,x, y, cnt):
    n = n//2
    if n > x and n <= y:
        y -= n
        cnt += n*n
    elif n <= x and n > y:
        x -= n
        cnt += 2*(n * n)
    elif n <= x and n <= y:
        x -= n
        y -= n
        cnt += 3 * (n * n)
    if n == 1:
        return cnt
    return Z_Search(n, x, y, cnt)

print(Z_Search(2**N, r, c, 0))