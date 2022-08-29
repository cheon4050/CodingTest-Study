def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(n**(1/2)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr

N = int(input())
tempArr = is_prime_num(N)
arr = []
check = False
for i in range(N+1):
    if tempArr[i]:
        arr.append(i)

start = 0
cnt = 0
result = 0
for end in range(len(arr)):
    cnt += arr[end]
    if N < cnt:
        while N < cnt:
            cnt -= arr[start]
            start +=1
    if N == cnt:
        result += 1
print(result)
