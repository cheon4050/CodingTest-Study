n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)] # 체크하기 위한 용도

for i in range(n): # n만큼 순서대로 for문 반복
    for j in range(i): # i전까지 순서대로 for문 반복
        if a[i] > a[j]: # 더 큰 수 가 있으면 max 함수로 값 저장
            dp[i] = max(dp[i], dp[j] + 1) # 첫번째는 1로 유지해야 해서 max 함수 사용

print(max(dp)) # 가장 긴 증가하는 부분 수열의 길이 출력