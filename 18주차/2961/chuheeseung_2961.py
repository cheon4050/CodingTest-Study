import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input()) # 재료의 개수 n
sour = [] # 신맛 리스트
bitter = [] # 쓴맛 리스트
diff = int(1e9)

for _ in range(n):
    a, b = map(int, input().split()) # 신맛과 쓴맛 리스트에 추가
    sour.append(a)
    bitter.append(b)

for i in range(1, n + 1): # 재료를 i개 뽑는 경우에 대해서 while문 반복
    cases = list(combinations(list(range(n)), i)) # 가능한 경우들을 담는 리스트
    # 개수가 적으니까 모든 경우 탐색

    for case in cases: # 리스트 경우 하나씩 for문 반복
        s = 1
        b = 0

        for j in range(i): # 맛 계산
            s *= sour[case[j]]
            b += bitter[case[j]]

        if abs(s - b) < diff: # 차이 계산
            diff = abs(s - b)

print(diff)
