from collections import deque

n, m = map(int, input().split())
arr = [0]*1000001
queue = deque([n])
while(queue):
    x = queue.popleft()
    move = [-1, 1, x]
    for i in range(3):
        temp_x = x + move[i]
        if temp_x < 0 or temp_x > 100000:
            continue
        else:
            if arr[temp_x] == 0:
                arr[temp_x] = arr[x]+1
                queue.append(temp_x)
            else:
                arr[temp_x] = min(arr[x]+1, arr[temp_x])
arr[n] = 0
print(arr[m])