n, k = map(int, input().split())
a = list(map(int, input().split()))
start = end = 0
d = {}
answer = 0
while end < n:
    d.setdefault(a[end], 0)
    if d[a[end]] < k:
        d[a[end]] += 1
        end += 1
    else:
        d[a[start]] -= 1
        start += 1
    answer = max(answer, end-start)
print(answer)
