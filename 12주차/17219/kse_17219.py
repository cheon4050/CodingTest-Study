dic={}
m,n=map(int,input().split())

for _ in range(m):
    s,p=input().split()
    dic[s]=p
for _ in range(n):
    s=input().rstrip('\n')
    print(dic[s])