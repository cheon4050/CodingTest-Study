def dp(r,c,n):
    startWith=paper[r][c] #첫번째 원소가 무엇으로 시작하는지 저장

    for i in range(r,r+n):
        for j in range(c,c+n):
            if paper[i][j]!=startWith: #같은숫자로 구성되지 않았으면
                n//=3 #9등분하기 위해 n//3

                for k in range(3):
                   for l in range(3):
                       dp(r+k*n, c+l*n, n) #잘린 9개 모두 재귀 호출
                return
    paperNumber[startWith+1]+=1 # 모두 같은 숫자라면 인덱스를 그숫자+1 로 하고 +1 해준다
    return

n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
paperNumber=[0]*3
dp(0,0,n)
print(*paperNumber,sep='\n')