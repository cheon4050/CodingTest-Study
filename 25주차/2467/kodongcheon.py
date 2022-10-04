N = int(input())
arr = list(map(int, input().split()))

start, end = 0, N-1
resultArr = []
while start < end:
    resultArr.append((abs(arr[end]+arr[start]),arr[start],arr[end]))
    if arr[end]+arr[start] > 0:
        end -= 1
    elif arr[end]+arr[start] == 0:
        print(arr[start], arr[end])
        break
    else:
        start+=1
else:
    resultArr.sort(key=lambda x : x[0])
    print(resultArr[0][1], resultArr[0][2])
