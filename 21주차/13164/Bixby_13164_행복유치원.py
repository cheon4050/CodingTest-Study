l=lambda:map(int,input().split())
n,k=l()
c=list(l())
print(sum(sorted([c[i]-c[i-1]for i in range(1,n)])[:n-k]))
#숏코딩 2등