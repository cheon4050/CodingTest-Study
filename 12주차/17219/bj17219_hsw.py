import sys

n, m = map(int, sys.stdin.readline().split())
passwords = dict()
for _ in range(n):
    url, password = sys.stdin.readline().split()
    passwords[url] = password
for _ in range(m):
    print(passwords[sys.stdin.readline().rstrip()])