import sys
from itertools import combinations
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    temp = [i for i in range(N)]
    result = int(1e9)
    for i in range(N):
        x, y = map(int,input().split())
        arr.append((x, y))
    for comb in list(combinations(temp,N//2)):
        not_comb = []
        for i in temp:
            if not i in comb:
                not_comb.append(i)
        vectors = []
        for i in range(N//2):
            vectors.append((arr[comb[i]][0]-arr[not_comb[i]][0],arr[comb[i]][1]-arr[not_comb[i]][1]))
        x, y = 0, 0
        for vector in vectors:
            temp_x, temp_y = vector
            x += temp_x
            y += temp_y
        result = min(result, math.sqrt(x*x + y*y))
    print(result)
