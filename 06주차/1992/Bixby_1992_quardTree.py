def dp(n,r=0,c=0):
    startWith=screen[r][c] #첫번째 원소가 무엇으로 시작하는지 저장

    for i in range(r,r+n):
        for j in range(c,c+n):
            if screen[i][j]!=startWith: #같은숫자로 구성되지 않았으면
                n//=2 #4등분하기 위해 n//2
                print("(",end='') #좌측 상단 결과 출력 전에 '('출력
                for k in range(2):
                   for l in range(2):
                       dp(n,r+k*n, c+l*n) #잘린 4개 모두 재귀 호출
                print(")",end='') #우측하단까지 끝나면 ')' 출력
                return
    print(startWith, end='') # 모두 같은 숫자라면 그 숫자를 출력
    return

n=int(input())
screen=[list(input()) for _ in range(n)]
dp(n)