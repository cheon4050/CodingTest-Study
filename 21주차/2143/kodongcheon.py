import sys
import collections
input = sys.stdin.readline

T = int(input())

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

ADict = collections.defaultdict(int)
BDict = collections.defaultdict(int)

for i in range(n+1):
    for j in range(i+1, n+1):
        ADict[sum(A[i:j])] += 1

for i in range(m+1):
    for j in range(i+1, m+1):
        BDict[sum((B[i:j]))] += 1

result = 0

for i in ADict:
    if T-i in BDict:
        result+=ADict[i]*BDict[T-i]

print(result)