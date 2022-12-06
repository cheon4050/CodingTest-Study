# 주어진 격자를 통해 만들어지는 빛의 경로 사이클의 모든 길이들을 배열에 담아 오름차순으로 정렬

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]  # 아, 왼, 위, 오른

def move(node, dir):   # 다음의 방향을 결정
    if node == 'L':    # 좌회전
        return (dir + 3) % 4
    elif node == 'R':  # 우회전
        return (dir + 1) % 4
    else:              # 직진
        return dir

def dfs(x, y, dir, grid, visit):
    cnt = 0      # 사이클의 길이
    R, C = len(grid), len(grid[0])

    while True:
        if visit[x][y][dir]:  # 이미 방문 했던 경로라면 사이클이 형성된 것이므로 종료
            break

        visit[x][y][dir] = True   # 해당 위치에서 해당 방향으로 가는 경로는 방문 표시
        dir = move(grid[x][y], dir)  # 방향 전환

        x = (x + dx[dir] + R) % R   # 배열을 벗어나는 경우 반대 방향으로 돌아오기
        y = (y + dy[dir] + C) % C
        cnt += 1
    return cnt


def solution(grid):
    R, C = len(grid), len(grid[0])
    visit = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]  # 각 방향에 대한 3차원 방문 배열 생성(같은 사이클인지 판별하기 위해)
    result = []

    for i in range(R):   # 각 노드들에 대해 상하좌우 모두 탐색
        for j in range(C):
            for k in range(4):
                if not visit[i][j][k]:   # 방문하지 않은 경로에 대해서만 탐색
                    result.append(dfs(i, j, k, grid, visit))
    return sorted(result)

print(solution(["SL", "LR"]))