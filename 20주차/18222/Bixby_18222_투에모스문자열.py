n=int(input())-1
ans=0
while(n):
    ans+=n%2
    n//=2
print(ans%2)