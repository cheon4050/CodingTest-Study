import sys
input = sys.stdin.readline
M = int(input())

sum = 0
for _ in range(M):
    n, s = map(int,input().split())
    sum += s * pow(n,1000000005,1000000007)
    sum %= 1000000007
print(sum)