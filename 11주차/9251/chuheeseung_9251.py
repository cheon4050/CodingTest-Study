import sys
input = sys.stdin.readline

word1, word2 = input().strip(), input().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    count = 0 # 누적변수로 사용
    for j in range(l2):
        # 누적변수값이 해당 위치의 캐시값보다 작은지부터 확인해야 한다
        if count < cache[j]: # 누적변수값 < 캐시값 : 교체
            count = cache[j]
        elif word1[i] == word2[j]: # 글자가 같은 경우 누적 변수 + 1
            cache[j] = count + 1

print(max(cache))

# 글자 하나를 기준으로 1차원 배열 생성
# 같은 글자를 순회하는 경우 누적값 + 1
# 순회할 때 마다 누적값을 저장할 변수 하나 사용
# 글자가 다른 경우 : 누적 변수의 값이 해당 위치의 값보다 작은 경우 해당 값으로 교체
# 누적값에는 이전 위치까지의 최대값이 계속해서 저장됨