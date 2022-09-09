import sys
input = sys.stdin.readline

def func(x1,y1,x2,y2, arr,result):
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[x1][y1] != arr[i][j]:
                result.append("(")
                #왼쪽 위
                func(x1,y1, x1+(x2-x1)//2, y1+(y2-y1)//2, arr, result)
                #오른쪽 위
                func(x1, y1 + (y2 - y1) // 2, x1 + (x2 - x1) // 2, y2, arr, result)
                #왼쪽 아래
                func(x1+(x2-x1)//2, y1, x2, y1+(y2-y1)//2, arr, result)
                #오른쪽 아래
                func(x1+(x2-x1)//2,y1+(y2-y1)//2, x2, y2, arr, result)
                result.append(")")
                return
    else:
        result.append(str(arr[x1][y1]))

N = int(input())
arr = []
result = []

for _ in range(N):
    temp = list(map(int,input().rstrip()))
    arr.append(temp)
func(0, 0, N, N, arr, result)

print("".join(result))
