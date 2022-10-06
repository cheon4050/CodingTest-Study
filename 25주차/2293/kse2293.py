'''
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.


그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
'''

# n,k= map(int, input())
# val = [int(input()) for i in range(n)]
n=3
k=10
val=[1,2,5]
dp = [0 for i in range(k+1)]

dp[0] = 1

for i in val:
    for j in range(i, k+1):
        dp[j] += dp[j-i]  # 이 동전으로 만들 수 있는 (가방 문제)
print(dp[k])
