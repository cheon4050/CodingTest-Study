T=int(input())
dxdy=[[-1,0],[0,1],[1,0],[0,-1]]
for i in range(T):
    queue=[]
    temp=0
    M,N,K=map(int,input().split())
    array=[[0 for j in range(M)]for k in range(N)]
    for j in range(K):
        arr1,arr2=map(int,input().split())
        array[arr2][arr1]=1
    for j in range(N):
        for k in range(M):
            if array[j][k]==1:
                temp+=1
                queue.append([j,k])
                array[j][k]=0
                while len(queue)>0:
                    arr2,arr1=queue.pop(0)
                    for a in range(len(dxdy)):
                        dx=arr2+dxdy[a][0]
                        dy=arr1+dxdy[a][1]
                        if 0<=dx<N and 0<=dy<M and array[dx][dy]==1:
                            array[dx][dy]=0
                            queue.append([dx,dy])
    print(temp)