n=int(input())
a=list(map(int,input().split()))
for i in range(1,n):
    a[i]=max(a[i-1]+a[i],a[i])
print(max(a))