N, K = map(int, input().split())

stack = []
for _ in range(N):
    A = int(input())
    stack.append(A)

cnt = 0
while stack:
    data = stack.pop()
    if K >= data:
        cnt += K // data
        K = K % data

print(cnt)