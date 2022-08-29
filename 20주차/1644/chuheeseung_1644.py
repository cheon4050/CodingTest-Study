import math, sys
input = sys.stdin.readline

n = int(input())

sosu = [True] * (n + 1) # 에라토스테네스의 체 -> 소수만 걸러줌
sosu[0] = False
sosu[1] = False

for i in range(2, int(math.sqrt((n))) + 1):
    if sosu[i]:
        for j in range(i * 2, n + 1, i):
            sosu[j] = False

sosu = [i for i in range(2, n + 1) if sosu[i]] + [0]

i = 0 # 투 포인터
j = 0
sum = sosu[i]
count = 0

while j < len(sosu) - 1:
    if sum == n: # 연속합이 n과 같은 경우
        count += 1
        sum -= sosu[i]
        i += 1 # 왼, 오 포인터 둘 다 한칸 진행
        j += 1 # 왼쪽만 옮기면 연속합이 감소해서 n보다 작아지니까 오른쪽도 옮겨줘야 함
        sum += sosu[j]
    elif sum < n: # 연속합이 n보다 작은 경우 -> 값을 키워줘야 한다는 뜻
        j += 1 # 오른쪽 포인터 + 1
        sum += sosu[j]
    else: # 연속합이 n보다 큰 경우 -> 값을 줄여줘야 한다는 뜻
        sum -= sosu[i]
        i += 1 # 왼쪽 포인터 진행

print(count)