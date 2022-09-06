import sys
input = sys.stdin.readline

n, s = map(int, input().split()) # n : 수열의 길이, s : 부분합 값
numbers = list(map(int, input().split()))
left, right = 0, 0 # 두개의 포인터는 0에서 시작
sum = 0 # 합을 저장하는 변수
min_length = sys.maxsize # 최대 길이로 초기화

while True:
    if sum >= s: # 총합이 s가 넘는 경우 : left를 옮기면서 어디까지 길이가 줄어드나 확인
        min_length = min(min_length, right - left)
        sum -= numbers[left]
        left += 1
    elif right == n:
        break
    else: # 총합이 s를 넘지 않는 경우 : right를 오른쪽으로 옮기면서 총합이 s를 넘을 때까지 더함
        sum += numbers[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)