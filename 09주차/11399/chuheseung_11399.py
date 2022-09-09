n = int(input())
p = list(map(int, input().split()))
num = 0

p.sort()

for i in range(n):
    for j in range(i + 1):
        num += p[j]

print(num)