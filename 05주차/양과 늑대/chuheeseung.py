# 현재 노드에서 어떤 노드를 갈 수 있는지 탐색
def getCanGoEdges(i, prev, graph):
    # i : 현재 위치, prev : 직전 노드 기준 갈 수 있는 노드, graph : 노드 간 연결 상태
    canGoEdges = [edge for edge in prev if edge != i]

    for j in range(len(graph)):
        if graph[i][j] == True:
            canGoEdges.append(j)

    return canGoEdges

# 현재 위치 i 기준으로 갈 수 있는 곳 탐색해서 양과 늑대의 수를 갱신
def dfs(i, s, w, prev, graph, info):
    global answer
    canGoEdges = getCanGoEdges(i, prev, graph)

    if s == w or not canGoEdges: # 종료 조건 : 양과 늑대의 개수가 같은 경우, 갈 수 있는 노드가 없는 경우 함수를 종료
        if answer < s:
            answer = s
        return

    for edge in canGoEdges:
        if info[edge] == 0: # 가려는 노드에 양이 있는 경우
            dfs(edge, s + 1, w, canGoEdges, graph, info)
        else: # 가려는 노드에 늑대가 있는 경우
            dfs(edge, s, w + 1, canGoEdges, graph, info)


def solution(info, edges):
    global answer
    answer = 1
    graph = [[False] * len(info) for _ in range(len(info))]

    for x, y in edges:
        graph[x][y] = True

    dfs(0, 1, 0, [0], graph, info)

    return answer


print(solution([0,0,1,1,1,0,1,0,1,0,1,1],
               [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

print(solution([0,1,0,1,1,0,1,0,0,1,0],
               [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))