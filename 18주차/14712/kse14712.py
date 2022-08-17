#넴모넴모
N, M = map(int, input().split())
board = [[0]*(M+1) for _ in range(N+1)]
dr=[-1,-1,0] #왼쪽위 대각선, 위, 왼
dc=[-1,0,-1]

# 사각형 검증
# 사각형이 있으면 결과값에 포함 X
# 사각형이 없으면 결과값 + 1

def dfs(r,c):
    total = 0
    cnt = 1

    if c >= M:
        r = r + 1
        c = 0
    if r >= N:
        return 0
    # 넣고
    board[r][c] = 1
    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue
        if board[nr][nc] :
            cnt=cnt+1

    if cnt < 4 :	#사각형이 만들어지지 않을때.. (3개 이하 넴모) ==> + 1
        total = total + 1 + dfs(r, c+1)
    # 안넣고
    board[r][c] = 0
    total = total + dfs(r, c+1)
    return total

# 이 함수로 호출하면 시간초과 뜸...
# def solve(r,c):
#     cnt = 1
#     for i in range(3):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if nr<0 or nr>=N or nc<0 or nc>=M:
#             continue
#         if board[nr][nc] :
#             cnt=cnt+1
#     return cnt

res = dfs(0,0)
print(res + 1)