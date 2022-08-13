from collections import deque
def calcTopologicalSort():
    queue = deque()
    for node in range(1,N+1):
        if link[node] == 0: # 시작점이라면...
            queue.append(node)
            result[node] = buildTime[node]
    while queue:
        curNode = queue.popleft()
        for node in matrix[curNode]:
            result[node]=max(result[node],result[curNode]+buildTime[node])
            link[node] -= 1 #진입차수 하나 빼기
            if link[node] == 0: #시작점 갱신
                queue.append(node)

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    result=[0]*(N+1) #각 노드까지 걸린 시간을 넣어둘 배열
    link=[0]*(N+1) #진입선
    matrix=[[] for _ in range(N+1)]
    buildTime = [0]+ list(map(int,input().split()))
    for _ in range(K):
        preNode, postNode = map(int, input().split())
        #그래프 만들기(나와있는 순서대로 그래프 만들어주면 될듯.)
        matrix[preNode].append(postNode)
        #postNode가 있다는 것은 그 postNode를 가리키는 preNode가 있다는 것이니까 진입차수를 늘려준다.
        link[postNode]+=1
    win = int(input())
    calcTopologicalSort()
    print(result[win])