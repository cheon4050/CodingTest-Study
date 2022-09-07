from collections import deque

n, l, r = map(int, input().split()) # 맵 크기, 인구 이동 가능 범위
graph = [list(map(int, input().split())) for _ in range(n)] # 인구 수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_count = 0

def process(x, y, index): # 특정 위치에서 출발 -> 모든 연합 체크 -> 데이터 갱신
    united = [] # (x, y) 위치와 연결된 연합 정보를 담는 리스트
    united.append((x, y))
    q = deque() # 탐색을 하기 위한 큐
    q.append((x, y))
    union[x][y] = index # 현재 연합 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수

    while q: # 큐가 빌 때까지 반복
        x, y = q.popleft()

        for i in range(4): # 현재 위치에서 상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    # 옆 나라와 인구 차이가 l 이상 r 이하인 경우
                    q.append((nx, ny)) # 연합에 추가
                    union[nx][ny] = index # 현재 연합 번호 할당
                    summary += graph[nx][ny] # 연합 전체 인구수 추가
                    count += 1 # 연합 국가 수 + 1
                    united.append((nx, ny)) # 연합 정보 리스트에 추가

    for i, j in united: # 연합 국가끼리 인구 분배
        graph[i][j] = summary // count

    return count

while True: # 인구 이동을 할 수 없을 때까지 반복
    union = [[-1] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n: # 모든 인구 이동이 끝난 경우
        break

    total_count += 1

print(total_count) # 인구 이동 횟수 출력