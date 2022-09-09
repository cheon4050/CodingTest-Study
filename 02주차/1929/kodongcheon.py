M, N = map(int, input().split())

arr = [True] * (N+1)
arr[1] = False
for i in range(2,N+1):
    if(arr[i] == True):
        if (i >= M):
            print(i)
        for j in range(i, N+1, i):
            arr[j] = False

