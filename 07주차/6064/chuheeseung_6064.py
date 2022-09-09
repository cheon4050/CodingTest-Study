def num(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0: # Q. 이걸 왜 하는거지?
            return x
        x += M
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(num(M, N, x, y))

# x에 m을 계속 더해나간 값 = y에 n을 계속 더해나간 값일 때 정답이 된다
# 카잉 달력의 마지막 해는 m과 n의 최소공배수