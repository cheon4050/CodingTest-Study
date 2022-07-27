N, X = map(int, input().split())

arr = list(map(int, input().split()))
cnt = sum(arr[:X])
result = cnt
temp = 1                                                                                                                                                                                                 
for i in range(X, N):
    cnt = cnt - arr[i-X] + arr[i]
    if result == cnt:
        temp +=1
    elif result < cnt:
        result = cnt
        temp = 1
if result == 0:
    print("SAD")
else:
    print(result)
    print(temp)