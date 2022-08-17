import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 행 개수 n, 열 개수 m
check = [[0 for _ in range(m)] for _ in range(n)] # 격자판

def dfs(x, y):
    count = 0

    if y >= m: # 열이 격자판을 넘어가는 경우
        x = x + 1 # 행을 하나 증가
        y = 0

    if x >= n: # 행이 격자판을 넘어가는 경우
        return 0 # 전부 탐색해서 탐색 끝냄

    # 왜 아래서부터 봐야 하는지 모르겠당 ㅇㅅaㅇ
    if check[x][y-1] == 0 or check[x-1][y-1] == 0 or check[x-1][y] == 0:
        check[x][y] = 1 # 넴모 놓음
        count += dfs(x, y + 1) + 1
        # 넴모 놓은 상태에서 재귀로 다음 경우 탐색, 그 결과에 현재 놓은 결과를 더해서 넣어줌
        check[x][y] = 0 # 다음 탐색을 해야 해서 다시 빈칸으로 돌려 놓음

    count += dfs(x, y + 1)

    return count

print(dfs(0, 0) + 1)