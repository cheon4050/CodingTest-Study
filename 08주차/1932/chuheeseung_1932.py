n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0: # 처음 -> 무조건 한칸 위 맨앞
            triangle[i][0] += triangle[i-1][0]
        elif j == len(triangle[i]) - 1: # 마지막 -> 무조건 한칸 위 맨 뒤
            triangle[i][j] += triangle[i-1][j-1]
        else: # 나머지 -> 대각선 왼쪽, 오른쪽 중 더 큰 것을 가져온다
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[n-1]))

