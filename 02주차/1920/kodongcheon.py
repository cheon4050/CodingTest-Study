import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr.sort()
result_arr = []
for i in range(len(arr2)):
    result_arr.append((i,arr2[i]))

result_arr = sorted(result_arr, key = lambda x:x[1])
result = [0]*M
cnt = 0
for idx, key in result_arr:
    while(True):
        if cnt == N:
            break
        if arr[cnt] == key:
            result[idx] = 1
            break
        elif arr[cnt] < key:
            cnt += 1
        else:
            break
for num in result:
    print(num)

