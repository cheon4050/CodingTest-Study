from collections import deque, defaultdict

def bfs(w, n, data): # bfs 탐색 및 연결된 노드 수 구하는 함수
    count = 1 # 연결된 노드 수
    visited = [False] * (n + 1) # 방문 여부 체크
    visited[w[0]] = True # 시작 노드 방문 처리
    queue = deque([w[0]])

    while queue: # bfs 탐색
        curr = queue.popleft()

        for i in data[curr]: # curr과 연결된 노드에 대해서 for문
            if visited[i] or i == w[1]: # 방문했거나 끊어지는 노드인 경우 패스
                continue

            count += 1
            queue.append(i)
            visited[i] = True

    return count

def solution(n, wires):
    answer = 10000
    data = defaultdict(set) # 각 노드별로 연결된 노드 정보
    for a, b in wires:
        data[a].add(b)
        data[b].add(a)

    for w in wires:
        temp = bfs(w, n, data) # 해당 와이어를 끊었을 때 한쪽 영역의 노드 수
        answer = min(answer, abs((n - temp) - temp))
        # 기존 answer와 현재 해당하는 와이어를 끊었을 때 노드 차이 비교해서 최솟값으로 변경

    return answer

n = 9 # 송전탑의 개수
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]] # 전선 정보
# [v1, v2] : v1, v2가 연결되어 있다
answer = solution(n, wires)
print(answer)