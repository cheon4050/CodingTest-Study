import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수 t

for _ in range(t):
    n, k = map(int, input().rstrip().split()) # 건물의 개수 n, 건설 순서 규칙의 총 개수 k
    d = list(map(int, input().rstrip().split())) # 각 건물 당 건설에 걸리는 시간 d
    graph = [[] for _ in range(n + 1)] # 건물 순서 규칙
    degree = [0 for _ in range(n + 1)] # 진입 차수
    dp = [0 for _ in range(n + 1)] # 해당 건물 건설까지 걸리는 시간
    queue = deque()

    for i in range(k):
        x, y = map(int, input().rstrip().split()) # 건설 순서 x, y (x 다음에 y 지음)
        graph[x].append(y) # 건물 규칙 입력 받아서 저장
        degree[y] += 1

    w = int(input().rstrip()) # 승리하기 위해 건설해야 할 건물의 번호 w

    for i in range(1, n + 1):
        if degree[i] == 0: # 진입 차수 가 0인 거는 큐에 넣어줌
            queue.append(i)
            dp[i] = d[i-1]

    while queue:
        tmp = queue.popleft()

        for i in graph[tmp]:
            degree[i] -= 1 # 진입 차수를 줄여주고 비용 갱신
            dp[i] = max(dp[i], dp[tmp] + d[i-1]) # dp 이용해서 건설 비용 갱신
            # 현재 자신의 dp값, 이전과 지금을 합한 값 비교

            if degree[i] == 0: # 진입 차수가 0이면 큐에 추가
                queue.append(i)

    print(dp[w])