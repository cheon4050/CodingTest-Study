import sys
input=sys.stdin.readline
n,m=map(int,input().split())
numbers=[list(map(int,input().split()))for _ in range(n)]
prefixsum=[[0]*(n+1)for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefixsum[i][j]=prefixsum[i][j-1]+prefixsum[i-1][j]-prefixsum[i-1][j-1]+numbers[i-1][j-1]
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    result=prefixsum[x2][y2]-prefixsum[x2][y1-1]-prefixsum[x1-1][y2]+prefixsum[x1-1][y1-1]
    print(result)