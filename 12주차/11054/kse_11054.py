n = int(input())
nums = list(map(int,input().split()))
# 가장 긴 증가수열을 저장할 dpp
dpp = [1 for _ in range(n)]
# 가장 긴 감소수열을 저장할 dpm
dpm = [1 for _ in range(n)]
# 가장 긴 바이토닉 수열을 저장할 dp
dp = [None]*n

# 가장 긴 증가수열 구하기
for i in range(1,n):
    for j in range(i):
        if nums[j]<nums[i]:
            dpp[i] = max(dpp[i],dpp[j]+1)

# nums를 뒤집은 rnums선언
rnums = nums[::-1]

# rnums의 가장 긴 증가수열
for i in range(1,n):
    for k in range(i):
        if rnums[k]<rnums[i]:
            dpm[i] = max(dpm[i],dpm[k]+1)

# dpm을 뒤집음
dpm=dpm[::-1]
for i in range(n):
    dp[i]=dpp[i]+dpm[i]-1

print(max(dp))
