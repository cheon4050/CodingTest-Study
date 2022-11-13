d=int(input()) #산책을 시작하고나서 지난 시간

route=[
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0],
] #행렬 만들어두기

num=1000000007

def solution(n):
        if n==1:
                return route
        temp=solution(n//2) #

        if n%2==1:
                return mult(mult(temp,temp), route) #m 행렬을 D번 거듭제곱한거 재귀로 계속 넣어주기
        else:
                return mult(temp,temp)


def mult(a,b): #a, b 두 행렬을 곱한 결과(행렬)을 반환
        spot = [[0] * 8 for _ in range(8)]
        for i in range(8):
                for j in range(8):
                        for x in range(8):
                                spot[i][j]+=a[i][x]*b[x][j]
                        spot[i][j]%=num
        return spot

print(solution(d)[0][0])