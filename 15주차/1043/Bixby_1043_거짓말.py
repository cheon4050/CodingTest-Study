l=lambda:input().split()
n,m=map(int,l())
k=set(l()[1:])
p=[set(l()[1:])for _ in range(m)]
for _ in range(m):
    for y in p:
        if y&k:k=k|y
c=0
for y in p:
    if not y&k:c+=1
print(c)