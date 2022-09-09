import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
result = []
for _ in range(T):
    p = input().rstrip()
    length = int(input())
    strr = input().rstrip()
    if strr == "[]":
        arr = []
    else:
        arr = deque(list(strr[1:-1].split(",")))
    state = False
    for i in range(len(p)):
        if p[i] == "R":
            state = not state
        elif p[i] == "D":
            if not arr:
                print("error")
                break
            if state:
                arr.pop()
            else:
                arr.popleft()
    else:
        if state:
            arr.reverse()
        print("["+",".join(arr)+"]")
