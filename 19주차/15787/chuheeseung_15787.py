import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(n)]
# 기차에는 20개의 좌석이 있으니까 원소 20개, 아직 아무도 안탔으니까 0으로 초기화
state = [] # 은하수를 통과한 기차의 상태를 저장하는 리스트
count = 0

for _ in range(m):
    a = list(map(int, input().split()))

    if a[0] == 1:
        train[a[1]-1][a[2]-1] = 1 # 좌석 값만 1로 바꿔준다

    elif a[0] == 2:
        train[a[1]-1][a[2]-1] = 0 # 좌석 값만 0으로 바꿔준다

    elif a[0] == 3:
        for j in range(19, 0, -1):
            train[a[1]-1][j] = train[a[1]-1][j-1] # 승객들 한칸씩 뒤로 이동
        train[a[1]-1][0] = 0 # 20번째 자리 사람 하차

    elif a[0] == 4:
        for j in range(19):
            train[a[1]-1][j] = train[a[1]-1][j+1] # 승객들 한칸씩 앞으로 이동
        train[a[1]-1][19] = 0 # 1번째 자리 사람 하차

for i in range(n):
    if train[i] not in state: # i번째 기차의 상태가 state 리스트에 없는 경우
        state.append(train[i]) # 리스트에 넣어주고
        count += 1 # count +1 증가

print(count)