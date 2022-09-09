import sys,collections as d
n=int(input())
a = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
print(round(sum(a)/n))
print(a[n//2])
c=d.Counter(a).most_common(2)
print(a[0] if n<2 else (c[1][0]if c[0][1]==c[1][1]else c[0]))
print(a[-1]-a[0])