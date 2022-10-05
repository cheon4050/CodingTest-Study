n=4 #도시의 개수
m=4 #도로의 개수
k=2 #거리 정보
x=1 #출발 도시의 번호

arr=[0,[2,3],[3,4]] #단방향 도로 정보
graph=[]
for i in range(1,n+1):
    graph.append(i)

print(graph)

if k==1:
    print(arr[x])
elif k>=2:
    graph.remove(*arr[x])

print(graph)