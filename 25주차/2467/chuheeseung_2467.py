import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split())) # 정렬된 채로 입력받음

l = 0 # 왼쪽 포인터
r = n - 1 # 오른쪽 포인터
curr = 0
answer = sys.maxsize
ansl = 0
ansr = 0

while l < r:
    if abs(liquids[l] + liquids[r]) < answer:
        answer = abs(liquids[l] + liquids[r]) # 두 용액을 더한 절댓값을 answer에 저장
        ansl = liquids[l]
        ansr = liquids[r]

    if liquids[l] + liquids[r] < 0: # 두 용액을 더한 값이 0보다 작으면 l + 1
        l += 1
    else: # 두 용액을 더한 값이 0보다 크면 r - 1
        r -= 1

print(ansl, ansr)