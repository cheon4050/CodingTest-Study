def solution(board, skill):
    # 누적합 용 배열 선언
    arr = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for skil in skill:
        typ, r1, c1, r2, c2, degree = skil
        # 누적합 배열에 비용 체크
        if typ == 1:
            arr[r1][c1] -= degree
            arr[r1][c2+1] += degree
            arr[r2+1][c1] += degree
            arr[r2+1][c2+1] -= degree
        else:
            arr[r1][c1] += degree
            arr[r1][c2+1] -= degree
            arr[r2+1][c1] -= degree
            arr[r2+1][c2+1] += degree
    result = 0
    #가로 방향 누적합 계산
    for i in range(len(arr)):
        for j in range(len(arr[0])-1):
            arr[i][j+1] += arr[i][j]
    #세로 방향 누적합 계산
    for j in range(len(arr[0])):
        for i in range(len(arr)-1):
            arr[i+1][j] += arr[i][j]
    #누적합 배열과 board값 계산하여 건물이 있는값 카운트
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+arr[i][j] > 0:
                result+=1
    return result

# def solution(board, skill):
#     arr = [[0]*(len(board[0])+1) for _ in range(len(board))]
#     for skil in skill:
#         typ, r1, c1, r2, c2, degree = skil
#         if typ == 1:
#             for i in range(r1, r2+1):
#                 arr[i][c1] -= degree
#                 arr[i][c2+1] += degree
#         else:
#             for i in range(r1, r2+1):
#                 arr[i][c1] += degree
#                 arr[i][c2+1] -= degree

#     result = 0
#     for i in range(len(board)):
#         cnt = 0
#         for j in range(len(board[0])):
#             cnt += arr[i][j]
#             board[i][j] += cnt
#             if board[i][j] >0:
#                 result +=1
#     return result
# # 정확성
# def solution(board, skill):
#     count = 0
#     for skil in skill:
#         typ, r1, c1, r2, c2, degree = skil
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 if typ == 1:
#                     board[i][j] -= degree
#                 else:
#                     board[i][j] += degree
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] >0:
#                 count += 1
#     return count

# kimjingo.tisotry.com/155