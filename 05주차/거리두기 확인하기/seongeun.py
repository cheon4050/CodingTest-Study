from collections import deque

def bfs(p):
    start = []

    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer


#P는 BFS 탐색을 시작할 때 다른 P를 만나거나 모든 탐색 가능한 지점을 방문할 때까지 상하좌우 이동을 반복한다. 그렇다면 이동 가능한 위치는 어디일까?

#탐색 중 파티션('X')를 만날 때
#P가 파티션('X')을 만나면 이는 벽에 가로막힌 것으로 해당 방향으로는 탐색이 불가능하다.

#탐색 중 빈 테이블('O')을 만날 때
#빈 테이블('O')은 마찬가지로 열려있는 공간이기 때문에 P가 탐색이 가능하다.

#탐색 중 또 다른 'P' 을 만날 때
#P가 이동을 계속 하다가 또 다른 P를 만나면 경로 거리를 판단해서 맨해튼 거리 2보다 작으면 거리두기 실패(return 0)을 판단하고 2보다 크면 거리두기 해당 P는 거리두기 성공을 의미한다. (P가 여러 개일 수 있으니 모든 P의 시작점에서 BFS 탐색에 성공해야 return 1을 반환해야함에 주의!)

#결과적으로 P의 다음 진행할 위치가 'O'이고 그 지점이 이미 방문하지 않은 곳일 때만 BFS를 진행하면 된다.