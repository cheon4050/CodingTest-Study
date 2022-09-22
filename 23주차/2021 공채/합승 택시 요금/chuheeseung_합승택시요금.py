from heapq import heappop, heappush

INF = int(1e9)
graph = [[]]

def dijkstra(s, f):
    global graph
    n = len(graph)
    distance = [INF for i in range(n)] # 최단거리 테이블을 INF 값으로 초기화
    distance[s] = 0 # 시작 노드로 가는 최단 거리는 0
    heap = [[0, s]] # 거리(금액), 노드 번호

    while heap:
        w, x = heappop(heap)

        if distance[x] < w: # 현재 노드가 이미 처리된 노드면 무시
            continue

        for item in graph[x]:
            _x, _cost = item[0], item[1]
            _cost += w

            if _cost < distance[_x]:
                distance[_x] = _cost
                heappush(heap, [_cost, _x])

    return distance[f]

def solution(n, s, a, b, fares):
    global graph
    answer = INF

    graph = [[] for i in range(n + 1)]

    for fare in fares: # graph 배열에 값을 다 넣어줌 (방향이 없는 그래프)
        s, f, cost = fare[0], fare[1], fare[2]
        graph[s].append([f, cost])
        graph[f].append([s, cost])


    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        # a와 b가 헤어지는 지점을 k라고 하는 경우
        # 요금 = dijkstra(출발점, k) + dijkstra(k, a의 도착점) + dijkstra(k, b의 도착점)
        # 주어진 지점들을 k에 대입해서 요금들을 비교 -> 최솟값을 찾아낸다

    return answer