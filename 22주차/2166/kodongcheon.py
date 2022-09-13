import sys
input = sys.stdin.readline
N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.append(arr[0])
cnt = 0
for i in range(N):
    cnt += arr[i][0]*arr[i+1][1]
cnt2 = 0
for i in range(N):
    cnt2 += arr[i][1]*arr[i+1][0]
result = cnt-cnt2
if result <0:
    result = -result
result /= 2
print("%.1f"%result)