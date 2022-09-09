def solution(n, k, cmd):
    #check[i] = i번 행이 존재한다면 O, 삭제되었다면 X
    check = ['O']*n
    #linked_list[i] = [prev, next] i번 행의 이전 행 번호 = prev, i행의 다음 행 번호 = next
    linked_list = {i:[i-1, i+1] for i in range(n)}
    #삭제된 행의 [prev, next, 행 번호]를 담는 스택
    stack = []
    #현재 선택된 행 번호
    cursor = k
    for command in cmd:
        #위로 X칸 이동
        if command[0] == 'U':
            x = int(command.split(" ")[1])
            #현재 선택된 행을 시작으로 연결된 prev 행을 따라 X번 이동해서 cursor 값을 갱신한다
            for _ in range(x):
                cursor = linked_list[cursor][0]
        #아래로 X칸 이동
        elif command[0] == 'D':
            x = int(command.split(" ")[1])
            #현재 선택된 행을 시작으로 연결된 next 행을 따라 X번 이동해서 cursor 값을 갱신한다
            for _ in range(x):
                cursor = linked_list[cursor][1]
        #현재 선택된 행 삭제
        elif command[0] == 'C':
            #현재 선택된 행의 이전 행 번호 prev, 다음 행 번호 next
            prev, next = linked_list[cursor][0], linked_list[cursor][1]
            #현재 선택된 행을 삭제 처리 한다
            check[cursor] = 'X'
            #prev와 next, 삭제된 행 번호를 stack의 top에 push
            stack.append([prev, next, cursor])
            #현재 삭제된 행이 가장 첫 행인 경우,
            if prev == -1:
                #현재 삭제된 행의 다음 행이 가장 첫 행이 된다
                linked_list[next][0] = prev
                #cursor를 현재 삭제된 행의 다음 행 번호로 갱신한다
                cursor = next
            #현재 삭제된 행이 가장 마지막 행인 경우,
            elif next == n:
                #현재 삭제된 행의 이전 행이 가장 마지막 행이 된다
                linked_list[prev][1] = next
                #cursor를 현재 삭제된 행의 이전 행 번호로 갱신한다
                cursor = prev
            #현재 삭제된 행이 중간에 있는 행인 경우,
            else:
                #현재 삭제된 행의 이전 행을 현재 삭제된 행의 다음 행과 연결해준다
                linked_list[prev][1] = next
                #현재 삭제된 행의 다음 행을 현재 삭제된 행의 이전 행과 연결해준다
                linked_list[next][0] = prev
                #cursor를 현재 삭제된 행의 다음 행 번호로 갱신한다
                cursor = next
        #가장 마지막에 삭제한 행 되돌리기
        elif command[0] == 'Z':
            #가장 마지막에 삭제한 행의 정보를 가져온다
            prev, next, idx = stack.pop()
            #idx 행을 되돌린다
            check[idx] = 'O'
            #idx 행의 이전 행 번호는 prev, 다음 행 번호는 next로 연결해준다
            linked_list[idx][0] = prev
            linked_list[idx][1] = next
            #되돌린 행이 첫 행인 경우,
            if prev == -1:
                #다음 행의 이전 행 번호를 되돌린 행으로 연결해준다
                linked_list[next][0] = idx
            #되돌린 행이 맨 마지막 행인 경우,
            elif next == n:
                #이전 행의 다음 행 번호를 되돌린 행으로 연결해준다
                linked_list[prev][1] = idx
            #되돌린 행이 중간에 있는 행인 경우,
            else:
                #이전 행의 다음 행 번호를 되돌린 행으로 연결해준다
                linked_list[prev][1] = idx
                #다음 행의 이전 행 번호를 되돌린 행으로 연결해준다
                linked_list[next][0] = idx
    return "".join(check)
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))