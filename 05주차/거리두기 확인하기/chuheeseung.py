from collections import deque

def bfs(p):
    start = [] # P에서 탐색을 시작하기 -> 탐색을 시작할 P를 담을 리스트

    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s]) # 큐에 초기값 넣음
        visited = [[0] * 5 for i in range(5)] # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)] # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0] # 좌우
            dy = [0, 0, -1, 1] # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0: # 범위 안에 있고 방문하지 않았을 때
                    if p[ny][nx] == 'O': # 다음 위치가 O이고 이미 방문하지 않은 곳일 때만 BFS를 진행하면 된다
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))