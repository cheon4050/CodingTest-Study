import sys
input = sys.stdin.readline

N = int(input())
arr = [[1] * N for i in range(N)]
result = 0
def dfs(cnt, arr):
    if cnt == N-1:
        global result
        result += sum(arr[cnt])
        return
    for i in range(N):
        if arr[cnt][i]:
            temp = [a[:]for a in arr]
            for k in range(N):
                temp[cnt][k] = 0
                temp[k][i] = 0
                if cnt + k <N and i+k<N:
                    temp[cnt+k][i+k] = 0
                if cnt + k < N and 0 <= i - k:
                    temp[cnt+k][i-k] = 0
                if 0 <= cnt - k and i + k < N:
                    temp[cnt-k][i+k] = 0
                if 0 <= cnt - k and 0 <= i - k:
                    temp[cnt-k][i-k] = 0
            dfs(cnt+1, temp)

dfs(0, arr)
print(result)