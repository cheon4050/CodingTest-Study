N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()
distanceList = []
for i in range(N-1):
    distanceList.append(arr[i+1]-arr[i])

distanceList.sort()

print(sum(distanceList[:N-K]))