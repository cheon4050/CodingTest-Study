import sys
from itertools import combinations
from bisect import bisect_left, bisect_right # 이진 탐색 라이브러리
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
left = arr[:n//2] # 왼쪽 부분 수열
right = arr[n//2:] # 오른쪽 부분 수열
leftSum = [] # 왼쪽 부분 수열의 합
rightSum = [] # 오른쪽 부분 수열의 합
answer = 0 # 부분 수열의 개수 저장할 변수

def getSum(arr, sumArr):
    for i in range(1, len(arr) + 1):
        for a in combinations(arr, i): # arr 배열에서 i개만큼 뽑아서 만드는 부분 집합
            sumArr.append(sum(a)) # 부분 집합의 합을 sumArr에 추가
    sumArr.sort()

def getNum(arr,find):
    return bisect_right(arr, find) - bisect_left(arr, find)
    # bisect_left(a, x) : 정렬된 a에 x를 삽입할 위치 리턴, x가 이미 있으면 기존 항목의 왼쪽 위치 리턴
    # bisect_right(a, x) : x가 이미 있으면 기존 항목의 오른쪽 위치 리턴

getSum(left, leftSum) # 왼쪽 부분 수열의 합을 저장
getSum(right, rightSum) # 오른쪽 부분 수열의 합을 저장

for l in leftSum:
    find = s - l
    answer += getNum(rightSum, find)

answer += getNum(leftSum, s)
answer += getNum(rightSum, s)

print(answer)