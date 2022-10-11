n=int(input()) #n일 뒤 백준이 퇴사
data = [list(map(int,input().split())) for _ in range(n)] #상담 기간과 금액 정보
dp=[0]*(n+2) #후에 n+1과 비교 해야해서 n+2로 사이즈를 잡는다.

for i in range(n,0,-1): #역순으로 탐색해서 찾는다.
    # print(i,data[i-1][0], i+data[i-1][0])
    if i+data[i-1][0]>n+1: # 만약 상담일이 n+1보다 크다면 퇴사 한 후이므로 커트
        dp[i] = dp[i+1]
    else: # 상담 가능한 경우
        dp[i]=max(dp[i+1], data[i-1][1]+dp[i+data[i-1][0]]) # 거꾸로 역순하면서 얻은 비용의 기존 값과(dp[i+1]) 그 전날(역순이므로)의 비용과 비교

print(dp[1])