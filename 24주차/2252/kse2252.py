from collections import deque

N,M = map(int,input().split()) # 학생 수, 학생 키 비교한 횟수
indegree = [0]*(N+1) #진입차수
graph = [[] for _ in range(N+1)]#간선 정보를 담은 리스트 (문제에서의 A,B)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b) # A가 B보다 작은 정보일 때 
    indegree[b]+=1 #B를 가리키는 A 진입차수 설정
'''
4 2
4 2
3 1
'''
#지금 graph 상황
# ex)       1 2 3 4
# 진입차수: 1 1 0 0
def topology_sort():
    q = deque()
    result = list()

    for i in range(1,N+1):
        if indegree[i]==0: #진입차수가 없을 때 큐에 넣기
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1

            if indegree[i]==0:
                q.append(i) #진입차수 없으면 시작점으로 돌리고 q에 넣기

    print(*result,sep=' ')

topology_sort()
    