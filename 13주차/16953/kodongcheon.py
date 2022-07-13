result = 100000000
def ss(n, cnt, target):
    global result
    if n > target:
        return
    elif n == target:
        result = min(result, cnt)
        return
    ss(n*2, cnt+1, target)
    ss(int(str(n)+"1"), cnt+1, target)

A, B = map(int, input().split())
ss(A, 1, B)
if result == 100000000:
    print(-1)
else:
    print(result)

