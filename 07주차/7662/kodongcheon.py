import heapq

t = int(input())

for i in range(t):
    k = int(input())
    q1, q2 = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()

        if com == 'I':
            heapq.heappush(q1, (int(num), j))
            heapq.heappush(q2, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else:
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)

    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    if not q1 or not q2:
        print("EMPTY")
    else:
        a = -q2[0][0]
        b = q1[0][0]
        print("%d %d" % (a, b))


# import heapq
# import sys
# input = sys.stdin.readline
# T = int(input())
# result =[]
# for _ in range(T):
#     N = int(input())
#     q1 = []
#     q2 = []
#     cnt = 0
#     for i in range(N):
#         s, num = input().rstrip().split()
#         num = int(num)
#         if s == "I":
#             heapq.heappush(q1, num)
#             heapq.heappush(q2, (-num, num))
#             cnt += 1
#         else:
#             if cnt == 0:
#                 q1 = []
#                 q2 = []
#                 continue
#             if num == -1:
#                 heapq.heappop(q1)
#             else:
#                 heapq.heappop(q2)
#             cnt -= 1
#     if cnt == 0 or (not q1 and not q2):
#         result.append('EMPTY')
#     else:
#         result.append((heapq.heappop(q2)[1], heapq.heappop(q1)))
# for i in range(len(result)):
#     if result[i] == 'EMPTY':
#         print('EMPTY')
#     else:
#         print(result[i][0], result[i][1])