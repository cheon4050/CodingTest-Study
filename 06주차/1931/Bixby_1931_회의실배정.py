n=int(input())
meetings=sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:(x[1],x[0]))
cnt=last=0
for start,end in meetings:
    if last<=start:
        last=end
        cnt+=1
print(cnt)