def dp(n,r=0,c=0):
    startWith=paper[r][c]

    for i in range(r,r+n):
        for j in range(c,c+n):
            if paper[i][j]!=startWith: #같은숫자로 구성되지 않았으면
                n//=2
                for k in range(2):
                    for l in range(2):
                        dp(n,r+k*n,c+l*n)
                return
    cnt[startWith]+=1            
    return

n=int(input())
cnt=[0]*2
paper=[list(map(int,input().split()))for _ in range(n)]
dp(n)
print(*cnt,sep='\n')
