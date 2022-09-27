import sys
input = sys.stdin.readline

def solution(n, w, dp):
    for i in range(n):
        for j in range(n):
            if not w[i][j]:
                w[i][j] = float('inf')

    for i in range(1, n):
        dp[i][0] = w[i][0]

    for k in range(1, n - 1):
        for route in range(1, size):
            if count(route, n) == k:
                for i in range(1, n):
                    if not isin(i, route):
                        dp[i][route] = get_minimum(n, w, i, route, dp)

    dp[0][size-1] = get_minimum(n, w, 0, size-1, dp)

    return dp[0][size-1]


def count(route, n):
    cnt = 0

    for n in range(1, n):
        if route & (1 << n - 1) != 0:
            cnt += 1

    return cnt

def isin(i, route):
    if route & (1 << i - 1) != 0:
        return True
    else:
        return False

def get_minimum(n, w, i, route, dp):
    minimum_dist = float('inf')

    for j in range(1, n):
        if isin(j, route):
            before_route = route & ~(1 << j - 1)
            dist = w[i][j] + dp[j][before_route]

            if minimum_dist > dist:
                minimum_dist = dist

    return minimum_dist

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
size = 2 ** (n - 1)
dp = [[float('inf')] * size for _ in range(n)]
print(solution(n, w, dp))