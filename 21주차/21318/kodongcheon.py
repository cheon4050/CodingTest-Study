import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
Q = int(input())
check = []
prefixSum = [0]

for i in range(N-1):
    if arr[i] > arr[i+1]:
        check.append(1)
    else:
        check.append(0)
    prefixSum.append(prefixSum[-1] + check[-1])


for _ in range(Q):
    x, y = map(int,input().split())
    x,y = x-1,y-1
    print(prefixSum[y]-prefixSum[x])
