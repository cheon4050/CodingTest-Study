from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]
numArr = set([i for i in range(N)])
result = 1000000

for k in range(1,N//2+1):
    combination = list(combinations(numArr, k))
    for com in combination:
        com2 = numArr-set(com)
        comSum = 0
        com2Sum = 0
        for i in com:
            for j in com:
                comSum += arr[i][j]
        for i in com2:
            for j in com2:
                com2Sum += arr[i][j]
        result = min(result, abs(comSum-com2Sum))
print(result)