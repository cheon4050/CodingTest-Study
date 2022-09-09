from heapq import*
import sys
input=sys.stdin.readline
h=[]
for _ in range(int(input())):
    x=int(input())
    if x:
        heappush(h,x)
    else:
        print(heappop(h)if h else 0)
