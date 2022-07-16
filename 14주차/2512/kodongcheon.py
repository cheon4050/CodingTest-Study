import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
target = int(input())
result = 0
def binary_search(arr, target, start, end):
    global result
    if start > end:
        return
    sum = 0
    mid = (start+end) // 2
    for i in arr:
        if i <= mid:
            sum += i
        else:
            sum += mid
    if sum == target:
        result = mid
        return
    elif sum < target:
        result = max(result, mid)
        binary_search(arr, target, mid+1, end)
    else:
        binary_search(arr, target, start, mid-1)
binary_search(arr, target, 0, 1000000000)
if sum(arr) <= target:
    print (max(arr))
else:
    print(result)