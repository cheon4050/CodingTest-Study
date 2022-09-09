a= input().split("-")
s=sum(map(int,a[0].split("+")))
if a[1:]:
    s-=sum(map(int,"+".join(a[1:]).split("+")))
print(s)