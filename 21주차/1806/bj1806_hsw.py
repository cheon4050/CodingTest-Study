import sys

n, s = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

temp = 0
left = right = 0
result = sys.maxsize
while right < n:
    temp += sequence[right]
    right += 1
    check = False
    while temp >= s:
        check = True
        temp -= sequence[left]
        left += 1
    if check:
        result = min(result, right - left + 1)
print(result) if result != sys.maxsize else print(0)