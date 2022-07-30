import sys
input = sys.stdin.readline
N, M, R = map(int,input().split())
arr = [list(map(int, input().split())) for i in range(N)]


def rotation(arr, x1, y1, x2, y2):
    temp = arr[x1][y1]
    for i in range(y1, y2):
        arr[x1][i] = arr[x1][i+1]
    for i in range(x1, x2):
        arr[i][y2] = arr[i+1][y2]
    for i in range(y2, y1, -1):
        arr[x2][i] = arr[x2][i-1]
    for i in range(x2, x1, -1):
        arr[i][y1] = arr[i-1][y1]
    if x1!=x2 and y1 != y2:
        arr[x1+1][y1] = temp
i = 1
cnt = min(N, M)//2
temp = []
for i in range(cnt-1, -1, -1):
    x1, y1, x2, y2 = i, i, N-1-i, M-1-i
    weight = x2-x1+1
    height = y2-y1+1
    temp.append(weight*height-sum(temp))
    for j in range(R%temp[-1]):
        rotation(arr, x1, y1, x2, y2)
for i in arr:
    for j in i:
        print(j, end = " ")
    print()

