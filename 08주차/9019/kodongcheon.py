from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    visited = [False] * 10000
    A, B = map(int,input().split())
    queue = deque()
    queue.append((A, ""))
    while queue:
        num, s = queue.popleft()

        if num == B:
            print(s)
            break

        temp = (num * 2) % 10000
        if not visited[temp]:
            visited[temp] = True
            queue.append((temp, s + "D"))

        temp = (num - 1) % 10000
        if not visited[temp]:
            visited[temp] = True
            queue.append((temp, s + "S"))

        front = num % 1000
        back = num // 1000
        temp = front*10 + back

        if not visited[temp]:
            visited[temp] = True
            queue.append((temp, s + "L"))

        front = num % 10
        back = num // 10
        temp = front * 1000 + back

        if not visited[temp]:
            visited[temp] = True
            queue.append((temp, s + "R"))
