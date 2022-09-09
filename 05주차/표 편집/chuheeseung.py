def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    up = ['blank'] + [x for x in range(n - 1)]
    down = [x for x in range(1, n)] + ['blank']
    delete_stack = []

    for command in cmd:
        c = command.split()

        if c[0] == 'U':
            count = int(c[1])
            for _ in range(count):
                k = up[k]

        elif c[0] == 'D':
            count = int(c[1])
            for _ in range(count):
                k = down[k]

        elif c[0] == 'C':
            delete_stack.append(k)
            answer[k] = 'X'

            # up[k] = blank : k가 현재 살아있는 리스트 중에서 맨 위에 있다는 뜻
            # 삭제 후에 아래에서 k를 재정의할 때 현재 k의 바로 아래칸으로 설정할 것
            # -> down[up[k]]를 설정하지 않아도 됨
            # down[k]도 마찬가지임
            # -> up[k], down[k]가 'blank'가 아닐 경우만 각각 체크하고 up, down 연결리스트를 업데이트해줌
            if up[k] != 'blank':
                down[up[k]] = down[k]
                # down[원래 k기준으로 한칸 위에 있는 친구] = 원래 k가 down됐을 때 친구
            if down[k] != 'blank':
                up[down[k]] = up[k]

            # 만약 기존의 k가 한 칸 더 내려갔을 때 blank면 맨 아래에 위치했다는 뜻
            # -> k를 기존의 k보다 한 칸 위로 설정
            # blank가 아니면 k보다 한칸 아래로 설정
            if down[k] != 'blank':
                k = down[k]
            else:
                k = up[k]

        elif c[0] == 'Z':
            d = delete_stack.pop()
            answer[d] = 'O'

            if up[d] != 'blank':
                down[up[d]] = d
            if down[d] != 'blank':
                up[down[d]] = d

    ans = ''

    for a in answer:
        ans += a

    return ans


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))