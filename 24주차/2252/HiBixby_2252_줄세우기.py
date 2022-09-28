from graphlib import*
t = TopologicalSorter()
def l(): return map(int, input().split())


n, m = l()
for _ in range(m):
    a, b = l()
    t.add(b, a)
for i in range(n):
    t.add(i+1)
print(*t.static_order())
