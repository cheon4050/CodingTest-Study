import sys
input = sys.stdin.readline
N, M = map(int, input().split())

name = {}
for _ in range(N):
    s, password = input().split()
    name[s] = password

for _ in range(M):
    s = input().rstrip()
    print(name[s])
