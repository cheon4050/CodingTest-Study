import heapq
import sys
n = int(input())
queue = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(queue,x)
    else:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue))