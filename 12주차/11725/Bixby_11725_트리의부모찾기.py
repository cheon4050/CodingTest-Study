n=int(input())
parents=[0 for i in range(n+1)]
alreadyExists={1}
for _ in range(n-1):
    a,b=map(int,input().split())
    if a in alreadyExists:
        parents[b]=a
        alreadyExists.add(b)
    else:
        parents[a]=b
        alreadyExists.add(a)
for i in range(2,n+1):
    print(parents[i])
