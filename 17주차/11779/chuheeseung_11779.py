import sys
import heapq
import copy
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    dis = [INF] * (n + 1) # 최소 비용을 담는 테이블
    dis[start] = 0 # 시작 지점은 0 넣음
    q = []
    heapq.heappush(q, (0, start))

    while q:
        now_cost, now_way = heapq.heappop(q)

        if dis[now_way] < now_cost:
            continue

        path[now_way].append(now_way) 
        # 자신의 최단 거리가 수정되면 자신을 통해서 도달하는 지점들의 최단 거리도 수정됨
        # 그 지점들의 최단 거리가 수정되면 경로도 수정해줘야 한다
        # 경로 = 현재 자신까지 도달한 최단 경로에서 자신을 추가한 것이 수정되는 지점의 최단 경로

        if now_way == end: # 우선순위 큐에서 뽑은 게 end랑 일치하면 비용값 리턴
            return dis[end]

        for new_cost, new_way in graph[now_way]: # 최단 거리 수정
            if dis[new_way] > new_cost + now_cost:
                dis[new_way] = new_cost + now_cost
                heapq.heappush(q, (dis[new_way], new_way))
                path[new_way] = copy.deepcopy(path[now_way]) # 최단 거리 수정 -> 최단 경로 수정

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)] # 인접 리스트
path = [[] for _ in range(n + 1)] # 경로 저장

for _ in range(m): # 그래프 정보 입력
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split()) # 시작점, 도착점
print(dijkstra(start)) # 최소 비용 출력
print(len(path[end])) # 경로 길이 출력
print(*path[end]) # 경로 출력