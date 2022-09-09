N = int(input())

arr = list(map(int, input().split()))

arr.sort()
temp = 0
result = 0
for p in arr:
    temp+= p
    result += temp

print(result)