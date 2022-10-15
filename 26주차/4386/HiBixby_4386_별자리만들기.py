def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    parent[max(a,b)]=min(a,b)
    return

n=int(input())
pos=[list(map(float, input().split()))for _ in range(n)]

parent=[i for i in range(n+1)]
tree=[]
result=0
for a in range(n-1):
    for b in range(a+1,n):
        x1,y1=pos[a]
        x2,y2=pos[b]

        D=((x1-x2)**2+(y1-y2)**2)**0.5
        tree.append((D,a,b))

for D,a,b in sorted(tree):
    if find(a)!=find(b):
        union(a,b)
        result+=D
print(result)