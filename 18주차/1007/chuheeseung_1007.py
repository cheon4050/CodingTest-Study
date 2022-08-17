import sys
import math
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 8)

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 점의 개수
    coords = [0 for _ in range(n)]
    xtotal, ytotal = 0, 0 # 모든 좌표들의 총합

    for i in range(n):
        x, y = map(int, input().split()) # 점의 좌표
        xtotal += x # 총합 값 갱신
        ytotal += y
        coords[i] = (x, y) # i번째 인덱스에 (x, y) 좌표 추가

    min_vector = 1000000

    comb = list(combinations(range(n), n // 2))
    for c in comb[: len(comb) // 2]: # 절반으로 안나누면 시간 초과
        xsum, ysum = 0, 0 # 더해야 하는 좌표의 총합

        for i in c:
            xsum += coords[i][0] # i번 점의 x값 더해주기
            ysum += coords[i][1] # i번 점의 y값 더해주기

        # 빼야 하는 좌표의 총합 = 모든 좌표의 총합 - 더해야 하는 좌표의 총합합
        xsum -= xtotal - xsum
        ysum -= ytotal - ysum
        vector = math.sqrt(xsum ** 2 + ysum ** 2) # 벡터 크기 구하기

        if min_vector > vector: # 최솟값 갱신
            min_vector = vector

    print(min_vector)