from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    tmp = deque(range(n))

    cnt = 0
    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            if tmp.popleft()==m:
                print(cnt)
                break
        else:
            q.rotate(-1)
            tmp.rotate(-1)