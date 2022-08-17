from collections import defaultdict
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
bagDict = defaultdict(int)
for i in range(N):
    M, V = map(int, input().split())
    arr.append((M, V))
for i in range(K):
    C = int(input())
    if C >= 1000000:
        C = 1000000
    bagDict[C] += 1
sortList = sorted(list(bagDict.keys()))

def binary_search(arr, target, start, end):
    cnt = -1
    while start <= end:
        mid = (start+end)//2
        if mid >= len(arr):
            break
        if target <= arr[mid]:
            if bagDict[arr[mid]] >= 1:
                cnt = arr[mid]
                end = mid - 1
            else:
                start = mid+1
        else:
            start = mid + 1
    return cnt

arr.sort(key= lambda x : (-x[1],x[0]))
result = 0
cnt = 0
for m, v in arr:
    if cnt == K:
        break
    idx = binary_search(sortList, m, 0, len(sortList))
    if idx == -1:
        continue
    else:
        bagDict[idx] -= 1
        if bagDict[idx] == 0:
            sortList.pop(sortList.index(idx))
            bagDict.pop(idx)
        result += v
        cnt += 1
print(result)
