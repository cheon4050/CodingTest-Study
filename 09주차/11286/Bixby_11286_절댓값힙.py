import sys
input= sys.stdin.readline
from heapq import*
h=[]
for _ in range(int(input())):
    x=int(input())
    if x:
        heappush(h,(abs(x),x))
    else:
        try:
            print(heappop(h)[1])
        except:
            print(0)