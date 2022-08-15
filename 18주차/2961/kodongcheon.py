from itertools import combinations
N = int(input())
arr1 = []
arr2 = []
for _ in range(N):
    a, b = map(int,input().split())
    arr1.append(a)
    arr2.append(b)
result = int(1e9)
arr = [i for i in range(N)]
for i in range(1,N+1):
    for j in list(combinations(arr, i)):
        temp1 = 1
        temp2 = 0
        for k in j:
            temp1 *= arr1[k]
            temp2 += arr2[k]
        result = min(result,abs(temp1-temp2))
print(result)