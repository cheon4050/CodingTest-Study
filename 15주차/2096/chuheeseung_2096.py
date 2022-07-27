import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
dp1 = temp
dp2 = temp

for _ in range(n-1):
    a, b, c = map(int, input().split())
    dp1 = [a + max(dp1[0], dp1[1]), b + max(dp1), c + max(dp1[1], dp1[2])] # dp 값 갱신
    dp2 = [a + min(dp2[0], dp2[1]), b + min(dp2), c + min(dp2[1], dp2[2])]

print(max(dp1), min(dp2))

# 왼쪽 : 그 전 선택이 왼쪽, 중간인 경우
# 중간 : 그 전 선택이 왼쪽, 중간, 오른쪽인 경우
# 오른쪽 : 그 전 선택이 중간, 오른쪽인 경우