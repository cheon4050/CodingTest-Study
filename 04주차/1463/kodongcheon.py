x = int(input())

arr = [0] * (3000001)
cnt = 1

while((arr[x]==0 or cnt <= x) and x != 1):
    if arr[cnt*3] > arr[cnt]+1 or arr[cnt*3] == 0:
        arr[cnt*3] = arr[cnt]+1
    if arr[cnt * 2] > arr[cnt] or arr[cnt*2] == 0:
        arr[cnt * 2] = arr[cnt] + 1
    if arr[cnt + 1] > arr[cnt] or arr[cnt+1] == 0:
        arr[cnt+1] = arr[cnt]+1
    cnt += 1
print(arr[x])