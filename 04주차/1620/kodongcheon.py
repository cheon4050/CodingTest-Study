import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
arrdict = {}
for i in range(n):
    str_in = input().strip()
    arr.append(str_in)
    arrdict[str_in] = i
for _ in range(m):
    str_in = input().strip()
    if str_in[0] >= "0" and str_in[0] <= "9":
        print(arr[int(str_in)-1])
    else:
        print(arrdict[str_in]+1)