import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    for i in list(map(int, input().split())):
        heappush(heap, i)
        if len(heap) == N+1:
            heappop(heap)
print(heappop(heap))
