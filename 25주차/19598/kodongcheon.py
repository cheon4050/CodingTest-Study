import sys
from heapq import *
input = sys.stdin.readline

heap = []
N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start,end))

arr.sort()
result = 0
for start, end in arr:
    if heap and start >= heap[0]:
        heappop(heap)
    heappush(heap, end)
    result = max(result, len(heap))

print(result)