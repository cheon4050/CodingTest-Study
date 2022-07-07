n, m = map(int, input().split())
dict = {}

for _ in range(n):
    site, password = input().split()
    dict[site] = password

for _ in range(m):
    find = input().rstrip()
    print(dict[find]) 