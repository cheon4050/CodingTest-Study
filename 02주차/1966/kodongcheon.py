from collections import deque
case = int(input())

for _ in range(case):
    n, m = map(int,input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    queue = deque()
    for i in range(n):
        queue.append((i,arr[i]))
    while(True):
        maxcnt = max(queue, key= lambda x : x[1])
        num = queue.popleft()
        if num[1] != maxcnt[1]:
            queue.append(num)
        else:
            cnt += 1
            if num[0] == m:
                print(cnt)
                break




