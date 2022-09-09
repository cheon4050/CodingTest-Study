import sys
from collections import Counter

n = int(sys.stdin.readline())

numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
    
numbers.sort() # 입력을 받은 후 정렬 먼저 하고 시작

# 1. 산술평균
print(round(sum(numbers) / len(numbers)))

# 2. 중앙값
print(numbers[len(numbers) // 2])

# 3. 최빈값
# Counter 모듈 -> 최빈값이 여러개인 경우를 고려해 빈도수가 가장 높은 2개를 반환
count = Counter(numbers).most_common(2) 
if len(numbers) > 1: 
    if count[0][1] == count[1][1]: # numbers의 길이가 2 이상인 경우 -> 두번째 작은 값 출력
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

# 범위
print(max(numbers) - min(numbers))