n = int(input())
seats = [list(map(int, input().split())) for _ in range(n*n)]

# n = 3
# seats = [[4, 2, 5, 1, 7], [3, 1, 9, 4, 5], [9, 8, 1, 2, 3], [8, 1, 9, 3, 4], [7, 2, 3, 4, 8], [1, 9, 2, 5, 7], [6, 5, 2, 3, 4], [5, 1, 9, 2, 8], [2, 9, 3, 1, 4]]

p = n*n
classroom = [[0] * n for _ in range(n)]

#print(classroom)

# 하 상 우 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(p):
    students = seats[i]
    tmp = []
    for j in range(n):
        for k in range(n):
            # 빈 칸 전부 고려
            if classroom[j][k] == 0:
                like = 0
                blank = 0
                # 주변 탐색
                for l in range(4):
                    nx, ny = j + dx[l], k + dy[l]
                    # 교실 범위 안이라면
                    if 0 <= nx < n and 0 <= ny < n:
                        if classroom[nx][ny] in students[1:]:
                            like += 1
                        if classroom[nx][ny] == 0:
                            blank += 1
                # 좋아하는 학생 수, 빈칸 수, 행, 열
                tmp.append([like, blank, j, k])
                #print(tmp)
    # like, blank는 내림차순 / 행, 열은 오름차순
    tmp.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    classroom[tmp[0][2]][tmp[0][3]] = students[0]

seats.sort()
result = 0


for i in range(n):
    for j in range(n):
        answer = 0
        # 주변 4 방향 탐색
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            # 교실 범위 안이면
            if 0 <= nx < n and 0 <= ny < n:
                # 주변 학생이 좋아하는 애 중 한명이라면
                if classroom[nx][ny] in seats[classroom[i][j]-1]:
                    answer += 1
        # 만족도 계산
        if answer != 0:
            result += 10 ** (answer-1)

print(result)