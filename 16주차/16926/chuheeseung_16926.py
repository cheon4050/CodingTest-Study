import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2): # 제한 조건 참고 -> min(n, m)을 2로 나눈 값 만큼 안으로 들어간다
        x, y = i, i # 돌려지는 배열 중 가장 첫번째 배열 인덱스
        temp = square[x][y]
        # 처음 시작할 때 값을 temp에 넣고 배열을 돌리다가 비어있는 배열에 temp 값을 넣어준다

        # 안쪽까지 계속 고려해야 해서 n-i, m-i까지로 범위 설정
        for j in range(i + 1, n - i): # 좌
            x = j
            prev_value = square[x][y]
            square[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i): # 하
            y = j
            prev_value = square[x][y]
            square[x][y] = temp
            temp = prev_value

        for j in range(i + 1, n - i): # 우
            x = n - j - 1
            prev_value = square[x][y]
            square[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i): # 상상            y = m - j - 1
            prev_value = square[x][y]
            square[x][y] = temp
            temp = prev_value

for i in range(n):
    for j in range(m):
        print(square[i][j], end=" ")

    print()

# 사각형을 좌 -> 하 -> 우 -> 상 순서로 바깥부터 돌아간다
# 하나의 사각형을 다 돌렸으면 안쪽 사각형으로 들어간다