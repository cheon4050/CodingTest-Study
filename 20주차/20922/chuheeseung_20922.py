import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split()) # 길이가 n인 수열, 같은 원소 k개 이하
numbers = list(map(int, input().rstrip().split())) # 수열
left, right = 0, 0 # 포인터 두개
answer = 0
counter = {}

while right < n: # 범위 안에서 while문 반복
    right_cnt = counter.get(numbers[right], 0)

    if right_cnt < k: # right 위치 개수 카운트가 k보다 작으면 계속 확장이 가능
        right_cnt += 1
        counter[numbers[right]] = right_cnt
        right += 1
    else:
        # right 위치 개수 카운트가 k 이하가 될 때 까지 left 포인터를 오른쪽으로 움직여서
        # 현재 right 포인터 수에 left 커서가 하나 올 때 까지 이동
        left_cnt = counter.get(numbers[left], 0)
        left_cnt -= 1
        counter[numbers[left]] = left_cnt
        left += 1

    answer = max(answer, right - left)

print(answer)