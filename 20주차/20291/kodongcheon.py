import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
extensionDict = defaultdict(int)
for i in range(N):
    name, extension = input().rstrip().split(".")
    extensionDict[extension] += 1

for extension, cnt in sorted(extensionDict.items()):
    print(extension, cnt)
