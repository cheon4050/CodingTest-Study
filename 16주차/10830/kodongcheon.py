import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, B = map(int,input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

def divide_conquer(A, B, n):
    if n == 1:
        temp = [[0] * (N) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    temp[i][k] = (temp[i][k] + A[i][j] * B[j][k]) % 1000
        return temp
    temp = divide_conquer(A, B, n//2)

    if n % 2 != 0:
        temp = divide_conquer(temp, arr, 1)

    return divide_conquer(temp, temp, 1)

result = divide_conquer(arr, arr, B//2)

if B % 2 != 0:
    result = divide_conquer(result, arr, 1)
for i in range(N):
    for j in range(N):
        print(result[i][j], end = " ")
    print()