import sys
input = sys.stdin.readline
C, N = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))
DP = [10000000] * (C+1+100)
C = C+100
DP[0] = 0
for i in range(C):
    for A, B in arr:
        if i-B >=0:
            DP[i] = min(DP[i], DP[i-B]+A)
print(min(DP[C-100:]))
