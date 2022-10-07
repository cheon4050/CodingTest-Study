from graphlib import*
l=lambda:map(int,input().split())
t=TopologicalSorter()
n,m=l()
for i in range(n):t.add(i+1)
for _ in range(m):
    a=list(l())
    for i in range(1,a[0]):t.add(a[i+1],a[i])
try:print(*t.static_order())
except:print(0)
#숏코딩 1등