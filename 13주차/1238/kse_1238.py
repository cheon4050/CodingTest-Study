import heapq
# n = 노드의 개수, m = 간선의 개수, x = 파티가 열리는 곳
n,m,x = map(int,input().split())
INF = int(1e9) # 10억을 무한으로 설정
go_graph = [[] for i in range(n + 1)] # 어떤 노드까지 가는데 걸리는 시간(비용)과  노드 -> 파티를 하기위해 파티장으로 감
back_graph = [[] for i in range(n + 1)] # 어떤 노드까지 가는데 걸리는 시간(비용)과 노드 -> 파티가 끝난 후 집으로 복귀
go_distance = [INF] * (n + 1) # 거리는 모두 무한으로 초기화
back_distance = [INF] * (n + 1) # 거리는 모두 무한으로 초기화

for i in range(m): # 출발노드, 도착노드, 시간(비용)정보를 받음
    a,b,c = map(int,input().split())
    go_graph[b].append((c,a)) # a번 노드에서 b번 노드로 가기 위한 시간(비용)
    back_graph[a].append((c,b)) # a번 노드에서 b번 노드로 가기 위한 시간(비용)

def dijkstra(start,graph,distance):
    distance[start] = 0 # 출발점에서 출발점 거리 = 0
    q = []
    heapq.heappush(q,(0,start))
    while q: # 큐가 빌때까지 반복
        cost,now = heapq.heappop(q) # cost = 목적지 노드까지의 비용, now = 노드
        for i in graph[now]: # graph[now]의 정보를 i에 담음
            # now 노드에서 목적지 노드까지의 비용 + 어떠한 노드까지의 비용이 현재 distance에 저장되어있는
            # 어떠한 노드에서 목적지 노드까지의 시간(비용)보다 작다면 if문 조건 실행
            if cost + i[0] < distance[i[1]]:
                # distance 업데이트 및 heappush
                distance[i[1]] = cost + i[0]
                heapq.heappush(q,(distance[i[1]],i[1]))

dijkstra(x,go_graph,go_distance) # 파티장에 가기위한 비용
dijkstra(x,back_graph,back_distance) # 파티가 끝난 후 다시 원래 위치로 돌아가기 위한 비용

max_value = 0 # 최댓값
for i in range(1, n + 1):
    max_value = max(max_value,go_distance[i] + back_distance[i]) # 왕복 시간(비용)이 가장 많이 소요되는 것을 탐색
print(max_value) # 최대 시간(비용) 출력