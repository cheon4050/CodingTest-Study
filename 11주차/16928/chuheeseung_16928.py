from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]
visited = [False] * 101
dist = [0] * 101
ladder, snake = dict(), dict()

for _ in range(n):
    s, e = map(int, input().split())
    ladder[s] = e

for _ in range(m):
    s, e = map(int, input().split())
    snake[s] = e

def bfs(i):
    q = deque()
    q.append(i) # 1을 q에 넣어주고 시작
    visited[i] = True

    while q:
        x = q.popleft()

        for k in dice:
            next = x + k # 현재 x번째 칸에서 k값을 더한 x+k가 다음 칸
            if 1 <= next <= 100: # 다음 칸에 사다리나 뱀이 있으면 next로 바꿔준다
                if next in ladder:
                    next = ladder[next]
                if next in snake:
                    next = snake[next]
                if not visited[next]: # 사다리나 뱀 없고 방문 안한 경우
                    q.append(next) # q에 next를 넣고 방문했다고 바꿔준다
                    visited[next] = True
                    dist[next] = dist[x] + 1 # 주사위를 굴린 횟수 + 1

bfs(1) # 처음에 1번 칸에서 시작
print(dist[100]) # 100번째 칸에 도착했을 때 주사위를 굴린 횟수 출력