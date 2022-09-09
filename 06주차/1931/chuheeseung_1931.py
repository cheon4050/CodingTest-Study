import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

array = sorted(array, key = lambda x : x[0]) # 시작 시간 기준으로 정렬
array = sorted(array, key = lambda x : x[1]) # 종료 시간 기준으로 정렬
# print(array)

count = 1 # 회의실을 최대로 사용할 수 있는 회의 수
last = array[0][1]

for i in range(1, n):
    if last <= array[i][0]: # 현재 회의 종료 시각이 다음 회의 시작 시각보다 작으면
        last = array[i][1] # 회의 종료 시각을 새로운 회의 배정 시각의 종료시각으로 업데이트
        count += 1 # 회의실을 새로 배정해줌

print(count)