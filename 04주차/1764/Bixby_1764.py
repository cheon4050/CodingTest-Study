#듣보잡
n,m=map(int,input().split())
res=sorted({input() for i in range(n)}&{input() for j in range(m)})
print(len(res),*res)