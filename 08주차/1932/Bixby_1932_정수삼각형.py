n=int(input()) # 삼각형의 크기
triangle=[list(map(int,input().split()))for _ in range(n)] #삼각형 입력 받기

for i in range(n-2,-1,-1): #n-2부터 0까지 역순으로
    for j in range(i+1):
        triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])