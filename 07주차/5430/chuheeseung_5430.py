import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    array = sys.stdin.readline().rstrip()[1:-1].split(",") # 숫자만 가져옴
    queue = deque(array)

    reverse, front, back = 0, 0, len(queue) - 1
    flag = 0

    if n == 0:
        queue = [] # []로 입력을 받아도 deque의 길이는 1 -> 예외로 빈큐로 초기화 해줘야 한다
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            reverse += 1 # 매번 실행하지 않고 뒤집는 횟수를 기억했다가 홀수일 때만 뒤집도록 함
        elif j == 'D':
            if len(queue) < 1: # 비어있는데 함수 실행하면 에러 발생
                flag = 1
                print("error")
                break
            else:
                if reverse % 2 == 0: # Q. 이 부분은 왜 하는거지? 이해 못함
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        if reverse % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")