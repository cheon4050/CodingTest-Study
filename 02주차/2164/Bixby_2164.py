import collections as c
n=int(input())
l=c.deque(range(1,n+1))
while len(l)>1:
    l.popleft()
    l.rotate(-1)
print(*l)