k = int(input())
cnt = 2**60
result = False
while cnt > 0:
    if k // (cnt+1) == 1:
        result = not result
        k -= cnt
    cnt //= 2
print(int(result))
