import math
f = math.factorial

n, m = map(int, input().split())

if n == m:
    print(1)
else:
    num = f(n) // (f(n-m) * f(m))
    print(num)