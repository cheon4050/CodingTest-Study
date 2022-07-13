import math

n, m = map(int, input().split())
print(math.factorial(n) // (math.factorial(n-m) * math.factorial(m)))

# 공식 : n! / {(n-m)! * m!}