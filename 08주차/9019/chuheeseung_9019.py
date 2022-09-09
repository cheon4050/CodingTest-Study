import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def order(num, case):
    if case == 'D':
        return (int(num) * 2) % 10000 # n을 두배로 바꾸고 결과값을 레지스터에 저장, 범위는 10000 미만
    elif case == 'S':
        return (int(num) - 1) % 10000 # n-1을 레지스터에 저장, 범위는 10000 미만
    elif case == 'L':
        temp = num // 1000 # n의 각 자릿수를 왼편으로 회전해서 레지스터에 저장 -> 2341
        return num % 1000 * 10 + temp
    elif case == 'R':
        temp = num % 10 # n의 각 자릿수를 오른편으로 회전해서 레지스터에 저장 -> 4123
        return num // 10 + 1000 * temp

d = ['D', 'S', 'L', 'R'] # for문을 돌아서 다음 경우를 확인할 리스트, 일반 BFS 문제에서 dx, dy 역할

def bfs(a, b, visited):
    q = deque([[a, ""]]) # a와 빈 문자열을 q에 넣어주고 시작
    visited[a] = 1 # a는 방문했다고 처리

    while q: # bfs 시작
        num, case = q.popleft()

        if num == b:
            print(case)
            break

        for i in range(4): # 현재 숫자에서 dslr을 적용하고 가능한 숫자를 구해준다
            n_case = order(num, d[i])

            if visited[n_case] == 0: # 가능한 숫자가 있으면, 가능한 숫자와 문자를 처음 ""로 시작한 문자열 뒤에 붙여준다
                q.append((n_case, case + d[i]))
                visited[n_case] = 1

for _ in range(t):
    visited = [0 for _ in range(10000)] # 조건에서 10000 미만이라고 했으니까 초기화 해준다
    a, b = map(int, input().split())
    bfs(a, b, visited)
