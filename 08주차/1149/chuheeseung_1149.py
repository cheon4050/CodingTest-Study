n = int(input())
houses = []

for _ in range(n):
    houses.append(list(map(int, input().split())))

for i in range(1, n):
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    houses[i][1] += min(houses[i - 1][0], houses[i - 1][2])
    houses[i][2] += min(houses[i - 1][0], houses[i - 1][1])

print(min(houses[-1]))

# 점화식 : 현재 R = 이전 G + 이전 B