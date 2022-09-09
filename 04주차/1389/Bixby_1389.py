from collections import deque
def bfs(st):
    #큐 구현을 위해 deque 라이브러리 사용
    queue=deque([st])
    #g현재 노드를 방문 처리
    visited[st]=1
    #큐가 빌때까지 반복
    while queue:
        #큐에서 하나의 원소 뽑기
        v=queue.popleft()
#        print(v,end=' ')#debug
        #해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # 방문여부 체크+카운팅
                visited[i]=visited[v]+1
 #   print(visited)#debug
    return sum(visited)

n,m= map(int,input().split())#유저의 수 n 친구 관계의 수 m
graph=[[] for _ in range(n+1)]#빈 그래프 생성
for _ in range(m):#친구 관계 입력받기(각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원리스트))
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
#print(graph)#debug
ans = []
for i in range(1, n+1):
    visited=[0]*(n+1)
    ans.append(bfs(i))
#print(ans)#debug
print(ans.index(min(ans))+1)#리스트 최소값 인덱스 가져오기(인덱스+1번째 친구의 케빈 베이컨 수가 가장 작다)