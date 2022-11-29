# 모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴개수

import math

def solution(n, stations, w):
    r = w * 2 + 1
    cnt, cur = 0, 0
    left = 1

    for s in stations:   # 맨 왼쪽과 중간 지역의 전파가 닿지 않는 공간 처리
        right = s - w

        if right > 1:   # left 지점과 같지 않다면 맨 앞에 전파가 닿지 않는 공간이 존재
            cnt += math.ceil((right - left) / r)    # 빈 공간에 세울 수 있는 기지국 개수 구하기(소수점 이라면 최소 한개가 더 필요하므로 아예 올림 처리)
        left = s + w + 1   # 왼쪽 지점을 다음 전파가 닿지 않는 공간의 시작으로 이동
        cur = s

    if cur + w < n:    # 중간 지역을 다 처리한 후 맨 오른쪽 빈 공간이 남아 있는 경우
        cnt += math.ceil((n - (cur + w)) / r)
    return cnt

print(solution(16, [9], 2))

# def spread(s, w, n, dp):  # 해당 위치 기준 전파를 전달 하는 함수
#     l = s - 1 - w
#     r = s - 1 + w
#
#     if 0 <= l < n:
#         for i in range(l, s):
#             dp[i] = 1
#
#     if 0 <= r < n:
#         for i in range(s, r + 1):
#             dp[i] = 1
