from collections import deque
n, k = map(int, input().split())
visited = [0 for i in range(100001)]
def bfs(v):
    q = deque() #큐 구현을 위해 deque 사용
    q.append(v) #수빈이 출발점 위치 큐에 삽입
    while q:
        v = q.popleft()
        #수빈이 위치가 동생의 위치와 같다면 반복문 종료
        if v == k:
            return visited[v]
        #이동할 수 있는 방향에 대해
        for i in (v-1, v+1, 2*v):
            # 주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0 <= i <= 100000 and not visited[i]:
                #이동한 위치에 현대 이동한 시간 표시
                visited[i] = visited[v] + 1
                #큐에 추가
                q.append(i)
print(bfs(n))