import itertools
n,m=map(int,input().split())
nPr=list(itertools.combinations(range(1,n+1),m))
for i in nPr:
    print(*i)