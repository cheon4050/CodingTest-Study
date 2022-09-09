n=int(input())
arr=[]
for i in range(n):
    a=[0]
    b=list(map(int,input().split()))
    arr.append(a+b+a)

for i in range(1,n):
    for j in range(1,i+2):
        arr[i][j]+=max(arr[i-1][j],arr[i-1][j-1])

print(max(arr[n-1]))