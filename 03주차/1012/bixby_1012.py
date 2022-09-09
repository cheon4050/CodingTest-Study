import sys
#재귀 리미트
sys.setrecursionlimit(10**6)
#테스트 케이스 만큼 반복
for T in range(int(input())):
    #m n k를 공백으로 구분하여 입력받기
    m,n,k=map(int,input().split())
    #2차원 리스트 초기화
    new=[[0]*n for _ in range(m)]
    #배추 위치 입력받기
    for _ in range(k):
        x,y=map(int,input().split())
        new[x][y]=1
    #DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def dfs(x,y):
        #주어진 범위를 벗어나는 경우 즉시 종료
        if x<0 or y<0 or x>=m or y>=n:
            return False
        #현재 노드를 아직 방문하지 않았다면
        if new[x][y]==1:
            #해당 노드 방문 처리
            new[x][y]=0
            #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
            return True
        return False
    cnt=0
    #모든 배추 그룹마다 배추흰지렁이 추가
    for x in range(m):
        for y in range(n):
            #현재 위치에서 dfs수행
            if dfs(x,y)==True:
                cnt+=1
    print(cnt) #정답 출력