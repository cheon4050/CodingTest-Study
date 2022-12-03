def solution(grid):
    # 각 방향을 수로 나타낼 딕셔너리 선언
    dir_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    n = len(grid)
    m = len(grid[0])

    # 현재 진행중인 방향과 다음 노드의 좌표를 입력받아 다음 방향을 설정하는 함수
    def next_dir(next_row, next_col, direction_number):
        next_dir_num = 0
        s = grid[next_row][next_col]
        # print(s)
        if s == 'S':
            next_dir_num = direction_number
        elif s == 'L':
            next_dir_num = (direction_number - 1) % 4
        elif s == 'R':
            next_dir_num = (direction_number + 1) % 4
        return next_dir_num

    answer = []
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)] #방향 확인용 리스트
    for row in range(n):
        for col in range(m):
            for num in range(4):
                if not visited[row][col][num]: #방문하지 않았나?
                    temp = 1
                    visited[row][col][num] = True
                    stk = [[row, col, num]]
                    while stk:
                        r, c, d = stk.pop()
                        # print("r:", r, " c: ", c, " d: ", d)
                        nr, nc = (r + dir_dict[d][0]) % n, (c + dir_dict[d][1]) % m
                        nd = next_dir(nr, nc, d)
                        # print(visited[nr][nc][nd])
                        if not visited[nr][nc][nd]:

                            temp += 1
                            # print(temp)
                            visited[nr][nc][nd] = True
                            stk.append([nr, nc, nd])
                        else:
                            # 방문을 했다면 순환의 시작점과 종료점이 같은지 확인
                            if [row, col, num] == [nr, nc, nd]: # 같다면 answer에 순환의 길이를 나타내는 temp 추가
                                answer.append(temp)
                        # print(answer)
    # print(answer)
    return sorted(answer)


print(solution(["SL","LR"]))