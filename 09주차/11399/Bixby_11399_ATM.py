n=int(input())
p=sorted(list(map(int,input().split())))
answer=0
for i in range(n):
    answer+=sum(p[:i+1])
print(answer)
