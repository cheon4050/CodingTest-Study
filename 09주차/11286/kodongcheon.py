import heapq
import sys
input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x),x))
