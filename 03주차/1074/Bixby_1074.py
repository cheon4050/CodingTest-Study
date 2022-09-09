n,r,c=map(int,input().split())
s=0
for i in range(n):
    s+=4**i*(r%2*2+c%2)
    r,c = r//2,c//2
print(s)