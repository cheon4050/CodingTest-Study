import heapq

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x),x))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)