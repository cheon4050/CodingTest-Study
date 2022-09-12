import sys
input = sys.stdin.readline
from collections import defaultdict
N, M = map(int, input().split())

Dict = defaultdict(int)
for i in range(N):
    s = input().rstrip()
    Dict[s] +=1
result = 0
for i in range(M):
    s = input().rstrip()
    result += Dict[s]
print(result)