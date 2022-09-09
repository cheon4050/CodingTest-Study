from collections import deque    
max_coor=10**5#최대 좌표
def bfs(start, k):
    q=deque([start])
    visited=[0]*(max_coor+1)   
    while q:#큐가 빌때까지
        #큐에서 하나의 원소를 뽑아서 k와 같은지 비교하고, 같으면 출력하고 프로그램 종료
        v=q.popleft()
        if v==k:
            print(visited[v])
            break
        for i in (v-1,v+1,v*2):
            if (0<=i<=max_coor) and not visited[i]:#좌표범위 안에 있고 아직 방문하지 않았다면 원소를 큐에 삽입
                visited[i]=visited[v]+1#방문체크+카운팅
                q.append(i)    
n,k=map(int,input().split())
bfs(n,k)