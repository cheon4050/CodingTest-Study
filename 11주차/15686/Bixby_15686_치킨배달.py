from itertools import combinations
n,m=map(int, input().split())
map=[list(map(int,input().split()))for i in range(n)]
homes=[]
chickenRestaurants=[]
for i in range(n):
    for j in range(n):
        if map[i][j]==1:
            homes.append((i,j))
        elif map[i][j]==2:
            chickenRestaurants.append((i,j))
selectedRestaurants=list(combinations(chickenRestaurants,m))
result=[0]*len(selectedRestaurants)
for home in homes:
    for i in range(len(selectedRestaurants)):
        tmp=1000
        for restaurants in selectedRestaurants[i]:
            chickenDistance=abs(home[0]-restaurants[0])+abs(home[1]-restaurants[1])
            tmp=min(tmp,chickenDistance)
        result[i]+=tmp
print(min(result))