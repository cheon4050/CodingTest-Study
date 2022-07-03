n,m=map(int,input().split())
d={}
for _ in range(n):
    k,v=input().split()
    d[k]=v
for _ in range(m):
    print(d[input()])