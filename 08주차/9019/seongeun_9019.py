from collections import deque

T = int(input())

for i in range(T):
    before, after = map(int, input().split())
    now = [(before, "")]
    dq = deque(now)
    cache = [False] * 10000
    cache[before] = True
    while dq:
        n, command = dq.popleft()
        if n == after:
            print(command)
            break

        # D
        D = (2 * n) % 10000
        if not cache[D]:
            dq.append((D, command + "D")) # D
            cache[D] = True

        # S
        if n != 0: # S
            S = n - 1
        else:
            S = 9999

        if not cache[S]:
            dq.append((S, command + "S"))
            cache[S] = True

        # L
        L = (n % 1000) * 10 + n // 1000
        if not cache[L]:
            dq.append((L, command + "L"))
            cache[L] = True

        # R
        R = (n % 10) * 1000 + n // 10
        if not cache[R]:
            dq.append((R, command + "R"))
            cache[R] = True