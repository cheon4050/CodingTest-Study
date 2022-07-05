# from collections import deque
#
# A, B, C = map(int,input().split())
#
# stack = deque()
# num = 1
# for i in range(B):
#     num = num*A
#     if num%C in stack:
#         break
#     stack.append(num%C)
# C = C - stack.index(num%C)
# for i in range(stack.index(num%C)):
#     stack.popleft()
# print(stack[C%len(stack)])

# a, b, c = map(int,input().split())
#
# def multi(a, n):
#     if n == 1:
#         return a % c
#     else:
#         tmp = multi(a, n // 2)
#         if n % 2 == 0:
#             return (tmp * tmp) % c
#         else:
#             return (tmp * tmp * a) % c
#
# print(multi(a, b))
a, b, c = map(int,input().split())
print(pow(a,b,c))