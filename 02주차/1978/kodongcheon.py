N = int(input())

arr = list(map(int, input().split()))

check_arr = [True]*1001
check_arr[1] = False
for i in range(2, 1001):
    if(check_arr[i] == True):
        for j in range(i*2, 1001, i):
            check_arr[j] = False
cnt = 0
for num in arr:
    if check_arr[num] == True:
        cnt += 1
print(cnt)
