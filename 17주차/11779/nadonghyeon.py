import sys
import heapq
import copy

input = sys.stdin.readline
INF = int(1e9)


# 다익스트라 함수
def dijkstra(start):
    dis = [INF] * (n + 1)  # 최소 비용 테이블
    dis[start] = 0  # 시작 지점 0 처리
    q = []
    heapq.heappush(q, (0, start))

    # 메인 로직
    while q:
        now_cost, now_way = heapq.heappop(q)

        if dis[now_way] < now_cost:
            continue

        # 최단 거리가 갱신되는 경우라면
        # 자기 자신을 통해 다른 곳으로 가는 지점의 경로 처리를 위해
        # 자기 자신 경로 테이블에 자기 자신 추가
        path[now_way].append(now_way)

        # 우선순위 큐에서 뽑은 것이 end와 일치하면 return
        if now_way == end:
            return dis[end]

        # 최단 거리 수정
        for new_cost, new_way in graph[now_way]:
            if dis[new_way] > new_cost + now_cost:
                dis[new_way] = new_cost + now_cost
                heapq.heappush(q, (dis[new_way], new_way))
                # 최단 거리 수정으로 인해 최단 경로 수정
                path[new_way] = copy.deepcopy(path[now_way])


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]  # 인접 리스트
path = [[] for _ in range(n + 1)]  # 경로 저장

# 그래프 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

# 시작점 도착점
start, end = map(int, input().split())
print(dijkstra(start))  # 최소 비용 출력
print(len(path[end]))  # 경로 길이
print(*path[end])  # 경로 출력