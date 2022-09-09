from collections import deque
def solution(places):
    result = []
    for place in places:
        check = True
        for i in range(len(place)):
            for j in range(len(place[0])):
                #P가 있는 시점마다 BFS 실행
                if place[i][j] == "P":
                    visited = [[0 for t in range(5)] for k in range(5)]
                    check = BFS(place, visited, i, j)
                # 거리두기 준수되지 않은 회의실이면 더 진행하지 않고 나가기
                if not check:
                    break
            if not check:
                break
        result.append(int(check))
    return result

#BFS 함수
def BFS(place, visited, a, b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while(queue):
        x, y = queue.popleft()
        # 상하 좌우 체크
        for i in range(4):
            temp_x = x+dx[i]
            temp_y = y+dy[i]
            # 배열을 벗어나거나, 방문했었거나, 막혀있는 곳이면 다음으로 패스
            if not (0 <= temp_x <= 4 and 0 <= temp_y <= 4) or visited[temp_x][temp_y] != 0 or place[temp_x][temp_y] == "X":
                continue
            # O이면 거리 +1
            elif place[temp_x][temp_y] == "O":
                queue.append((temp_x, temp_y))
                visited[temp_x][temp_y] = visited[x][y] + 1
            # P를 만났는데, 첫 시작위치가 아니고, 거리가 2 이하이면 False
            elif place[temp_x][temp_y] == "P" and visited[x][y] < 3 and (temp_x != a or temp_y != b):
                return False
    else:
        return True