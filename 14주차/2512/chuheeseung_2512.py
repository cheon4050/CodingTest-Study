import sys
input = sys.stdin.readline

n = int(input()) # 지방의 개수
budget = list(map(int, input().split())) # 예산 리스트
m = int(input()) # 총 예산
start, end = 0, max(budget) # 가장 작은 금액(start):0, 가장 큰 금액(end):max(budget)

while start <= end: # 이분 탐색
    mid = (start + end) // 2 # 상한액 설정
    curr = 0

    for i in budget:
        if i >= mid: # 요청 금액이 상한액 이상인 경우
            curr += mid # 상한액 더하기
        else: # 요청 금액이 상한액 미만인 경우
            curr += i # 요청 금액 더하기

    if curr <= m: # 예산 총액이 총 예산 이하인 경우
        start = mid + 1
    else: # 예산 총액이 총 예산을 초과하는 경우우
       end = mid - 1

print(end)
