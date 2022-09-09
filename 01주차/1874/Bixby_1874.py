cnt = 0
s=[]
res=[]
for i in range (int(input())):
    n = int(input())
    while cnt < n:
        cnt+=1
        s.append(cnt)
        res.append("+")
    if s[-1] == n:
        s.pop()
        res.append("-")
    else:
        print("NO")
        exit()
print("\n".join(res))