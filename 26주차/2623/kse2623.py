from collections import deque

N, M = map(int,input().split()) #가수의 수/보조 PD의 수

graph = [[] for _ in range(N+1)] # 순서가 들어갈 그래프
indegree = [0] * (N+1)
for i in range(M):
    data = list(map(int,input().split())) #정해둔 순서
    for j in range(1,data[0]):
        graph[data[j]].append(data[j+1]) #순서에 따라 a,b정의 (a보다 b가 뒷 순서)
        indegree[data[j+1]]+=1

#위상정렬
q = deque()
result = []
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
        result.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            result.append(i)

if len(result) != N: #불가능
    print(0)
else:
    for r in result:
        print(r)