import heapq
import sys

input = sys.stdin.readline

minHeap = []
num = int(input())

for _ in range(num):
    n = int(input())

    if n == 0:
        if(len(minHeap)):
            print(heapq.heappop(minHeap))
        else:
            print(0)
    else:
        heapq.heappush(minHeap, n)





# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32