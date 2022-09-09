import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)] # 그래프 생성
visited = [[0] * n for _ in range(n)] # 방문 여부를 기록할 그래프 생성
houses = []
house = 0

def search(i, j): # 탐색하는 함수
    global house

    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] == '0': # 종료 조건
        return

    graph[i][j] = '0' # 탐색한 지점을 0으로 변경
    visited[i][j] = 1 # 방문한 정점 표시
    house += 1 # 단지 수 갱신

    search(i + 1, j) # 상하좌우 탐색
    search(i, j + 1)
    search(i - 1, j)
    search(i, j - 1)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == '1':
            search(i, j)
            houses.append(house)
            house = 0

print(len(houses))
for i in sorted(houses):
    print(i)