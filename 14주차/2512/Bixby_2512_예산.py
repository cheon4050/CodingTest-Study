n = int(input())
request = list(map(int, input().split()))
m = int(input())
left = 0
right = max(request)
while left <= right:
    mid = (left+right)//2
    sum = 0
    for r in request:
        sum += r if r < mid else mid
    if sum <= m:
        left = mid+1
    else:
        right = mid-1
print(right)
