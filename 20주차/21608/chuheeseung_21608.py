import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * n for _ in range(n)]
# 입력 받은 걸 한번에 리스트에 넣어줌
students = [list(map(int, input().split())) for _ in range(n ** 2)]
r = [-1, 1, 0, 0]
c = [0, 0, 1, -1]
score = 0

for order in range(n ** 2): # 학생수만큼 for문 돌면서 자리에 앉혀준다
    student = students[order]
    temp = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                empty = 0

                for k in range(4): # arr[i][j]의 상하좌우 탐색
                    nr, nc = i + r[k], j + c[k]

                    if 0 <= nr < n and 0 <= nc < n: # 범위 안에 있는 경우
                        if arr[nr][nc] in student[1:]: # 좋아하는 학생이 자리에 있는 경우
                            like += 1
                        if arr[nr][nc] == 0: # 자리가 비어 있는 경우
                            empty += 1

                temp.append([like, empty, i, j]) # tmp 배열에 추가

    temp.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))
    # like, blank는 클수록, 행과 열의 수는 작을수록 답이니까
    # 1,2번째 인자는 내림차순, 3,4번째 인자는 오름차순으로 정렬
    arr[temp[0][2]][temp[0][3]] = student[0] # 정렬 후 학생을 자리에 앉힘

students.sort() # 학생 순서대로 점수를 주기 위해 정렬

for i in range(n): # 점수 매기기
    for j in range(n):
        answer = 0
        for k in range(4):
            nr, nc = i + r[k], j + c[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    answer += 1
        if answer != 0:
            score += 10 ** (answer - 1)

print(score)