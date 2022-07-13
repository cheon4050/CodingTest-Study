from collections import deque


# 1 2가 입력이 들어올 때 2를 곱했던 것이 0초가 되서 최소 값인데
# 방문체크가 없으면 +1로 1초가 되므로 방문체크를 사용해야한다
def bfs():
    q = deque()
    q.append(N)
    visited[N] = True
    while q:
        x = q.popleft()
        if x == K:
            return
        # 2를 곱했을 때 방문 범위를 벗어나지 않고 방문하지 않았을 때
        if 2 * x <= 100000 and not visited[2 * x]:
            q.appendleft(2 * x) # 우선순위가 높기 때문에(K에 더 가까워짐) 큐에서 맨 앞으로 추가해준다
            numbers[2 * x] = numbers[x]
            visited[2 * x] = True
        # 1을 더했을 때 방문하지 않았다면 방문
        if x + 1 <= 100000 and not visited[x + 1]:
            q.append(x + 1)
            numbers[x + 1] = numbers[x] + 1 # 1초 추가
            visited[x + 1] = True
        # 1을 뺐을 때 방문하지 않았다면 방문 ( 0보다 크거나 같아야 한다. 안그러면 인덱스 에러 )
        if x - 1 >= 0 and not visited[x - 1]:
            q.append(x - 1)
            numbers[x - 1] = numbers[x] + 1 # 1초 추가
            visited[x - 1] = True


N, K = map(int, input().split())
visited = [False] * 100001
numbers = [0] * 100001
bfs()
print(numbers[K])