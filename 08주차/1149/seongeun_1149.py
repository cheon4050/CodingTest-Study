n = int(input())
arr = []
RGB = [0,1,2]

for _ in range(n):
    arr.append(list(map(int, input().split())))

cost = arr[0]

for rgb in arr[1:]:
    r = rgb[0] + min(cost[1], cost[2]) #cost[1]=40 -> min(40,83)
    g = rgb[1] + min(cost[0], cost[2])
    b = rgb[2] + min(cost[0], cost[1])
    cost = [r, g, b]

print(min(cost))