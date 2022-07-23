N, M = map(int, input().split())
arr = list(map(int,input().split()))

cnt = 0
arr2 = []
for i in range(M):
    temp = list(map(int, input().split()))[1:]
    arr2.append(temp)

for _ in range(len(arr2)):
    for i in arr2:
        for j in i:
            if j in arr[1:]:
                arr = arr+i
                break
if arr[0] == 0:
    print(M)
else:
    arr = list(set(arr[1:]))
    for i in arr2:
        for j in i:
            if j in arr:
                break
        else:
            cnt+=1
    print(cnt)