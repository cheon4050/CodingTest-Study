N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
result = 0
def dfs(arr, cnt):
    global result
    if cnt == len(arr):
        temp = 0
        for i in range(len(arr)):
            if arr[i][0] <= 0:
                temp+=1
        result = max(result, temp)
    elif arr[cnt][0] < 0:
        dfs(arr,cnt+1)
    else:
        flag = False
        for i in range(len(arr)):
            if arr[i][0] <= 0 or cnt == i:
                continue
            tempArr = [i[:] for i in arr]
            tempArr[cnt][0] -= tempArr[i][1]
            tempArr[i][0] -= tempArr[cnt][1]
            dfs(tempArr, cnt+1)
            flag= True
        if not flag:
            dfs(arr,cnt+1)
dfs(arr,0)
print(result)