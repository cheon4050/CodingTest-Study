a,b=map(int,input().split())
i=1
while b>a:
    if b%10==1:
        b//=10
    else:
        b/=2
    i+=1
print([-1,i][a==b])