n,m=map(int,input().split())
a={i+1:input().strip() for i in range(n)}
b={v:k for k,v in a.items()}
for _ in range(m):
    c=input().strip()
    print(b[c] if c in b else a[int(c)])
#pypy3