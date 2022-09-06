from collections import deque
R, C = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = [list(input().rstrip()) for _ in range(R)]
chk = [0]*26

dq = deque()

dq.append((0, 0, 1)) # x,y 좌표, 중복 카운트 1부터 시작
chk[ord(board[0][0]) - ord('A')] = 1 #유니코드 정수를 반환
max_cnt = 0
print(dq)
while dq:
    tmp = dq.popleft() #이거 안넣어주면 더 오래걸림 popleft 자체가 O(1)
    print(f'좌표 : {tmp[0]},{tmp[1]} -> {board[tmp[0]][tmp[1]]} , 중복카운트 : {tmp[2]} , 최대값 : {max_cnt} ')
    for i in range(4):
        yy = tmp[0] + dy[i]
        xx = tmp[1] + dx[i]
        cnt = tmp[2]
        max_cnt = cnt if max_cnt < cnt else max_cnt

        if (0 <= yy <= R-1 and 0 <= xx <= C-1) and (chk[ord(board[yy][xx])-ord('A')] == 0):
            chk[ord(board[yy][xx]) - ord('A')] = 1
            cnt += 1
            dq.append((yy, xx, cnt))
        else:
            continue
print(max_cnt)

'''
2 4
CAAB
ADCB
-->
좌표 : 0,0 -> C , 중복카운트 : 1 , 최대값 : 0 
좌표 : 1,0 -> A , 중복카운트 : 2 , 최대값 : 1 
좌표 : 1,1 -> D , 중복카운트 : 3 , 최대값 : 2 
'''