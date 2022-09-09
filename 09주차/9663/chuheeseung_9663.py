def adjacent(x): # x윗줄에 겹치는 라인에 퀸이 있는지 확인하는 함수
    for i in range(x): # 인덱스 : 행, row[n]값 : 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같은 경우 False
            return False # 대각선이 같은 경우 : 두 좌표에서 행-행=열-열이 같은 것
    return True

def dfs(x): # 한줄씩 재귀하면서 dfs를 실행
    global result

    if x == n:
        result += 1
    else: # 각 행에 퀸을 놓는다
        for i in range(n): # i는 0열 ~ n-1열 돌면서 가능한 곳을 찾는다
            row[x] = i # i : 열번호
            if adjacent(x): # 행, 열, 대각선을 체크해서 True를 리턴하면 백트래킹 안하고 계속 진행
                dfs(x + 1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)

# 1. n개의 퀸을 배치해야 함 -> 무조건 모든 행에 퀸이 들어가야 한다
# 2. 0열부터 n-1열까지 퀸을 놓는 방법을 for문을 통해서 돌린다
# 3. 이전의 열로 인해서 영향을 받는지 검사하는 adjacent()를 통해서 가능한 것만 걸러준다