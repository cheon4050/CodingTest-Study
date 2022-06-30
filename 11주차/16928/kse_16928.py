#1부터 시작하여 가능한 주사위의 눈이 1~6 이므로 모든 경우를 큐에 넣는다.
#이 때, 다음 노드가 뱀 또는 사다리에 연결되어 있다면 반드시 이동해야 하므로
#즉시 연결된 노드로 이동한다.
#범위 내에서 아직 방문하지 않은 경우 주사위 횟수를 추가하고 다음 노드를 큐에 넣는다.

#list대신 dictionary 쓴 이유 : 뱀과 사다리의 번호가 서로 중복되지 않기 때문에 kwy를 통해 뱀과 사다리의
#도착점을 O(1)만에 찾기 위해서임.
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 0

    while queue:
        v = queue.popleft()
        for i in range(1, 7):
            y = v + i
            if y > 100:
                continue
            y = graph[y]
            if visited[y] == -1 or visited[y] > visited[v] + 1:
                visited[y] = visited[v] + 1
                queue.append(y)


N, M = map(int, input().split())

graph = [*range(101)]
visited = [-1] * 101

for _ in range(N + M):
    x, y = map(int, input().split())
    graph[x] = y

bfs(graph, 1, visited)
print(visited[-1])

#이동을 했을 때 94에 도착을 했고, 근데 그 94 자리에 94->90이라느 뱀이 존재하면 "94로 이동 후
#뱀에 의해서 90으로 이동할게되고 한 번의 횟수로 세어진다. 이를 위해 94에 방문하지
#않은 것으로 표시하고 대신 90을 방문한 것으로 표시해야함.
#그럼 100까지 가는 방법이 93->99->100