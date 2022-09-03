import sys
from heapq import *
input = sys.stdin.readline
N, K = map(int, input().split())

arr = list(map(int,input().split()))
heap = []
result = arr[-1] - arr[0]

for i in range(N-1):
    heappush(heap, -(arr[i+1]-arr[i]))
for i in range(K-1):
    result += heappop(heap)

print(result)