import sys
import heapq
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

# 그리디
def multiple(a, count):
    return count + 1, a * 2

def add(a, count):
    return count + 1, int(str(a) + "1")

def aToB(a, b):
    q = [(0, a)]

    while q:
        count, a = heapq.heappop(q)

        if a < b:
            # 둘 다 count 똑같이 1 증가하고 heapq에 넣어줘서 두 연산을 한번에 해도 상관없는건가?
            heapq.heappush(q, multiple(a, count))
            heapq.heappush(q, add(a, count))
            print(a, count, q)
        elif a == b:
            return count + 1
        else:
            continue

    return -1

print(aToB(a, b))

# bfs
# def aToB(a, b):
#     q = deque([(a, 1)])
#
#     while q:
#         a, count = q.popleft()
#
#         if a == b:
#             print(count)
#             return
#
#         if a * 2 <= b:
#             q.append((a * 2, count + 1))
#         if a * 10 + 1 <= b:
#             q.append((a * 10 + 1, count + 1))
#
#     print(-1)

# aToB(a, b)