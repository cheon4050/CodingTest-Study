import sys
input = sys.stdin.readline
n, m = map(int, input().split())
result = []
dictionary = {}
for _ in range(n):
    name = input().strip()
    dictionary[name] = 1
for _ in range(m):
    name = input().strip()
    if name in dictionary:
        result.append(name)
print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])