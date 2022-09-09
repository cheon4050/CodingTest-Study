N = int(input())

arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)

result0 = [0] * (max(arr)+1)
result1 = [0] * (max(arr)+1)
def fibonacci1(n):
    if result1[n] != 0:
        return result1[n]
    elif n == 0:
        return 0
    elif n == 1:
        result1[n] = 1
        return 1
    else:
        result1[n] = fibonacci1(n-1)+fibonacci1(n-2)
        return result1[n]
def fibonacci0(n):
    if result0[n] != 0:
        return result0[n]
    elif n == 0:
        result0[n] = 1
        return 1
    elif n == 1:
        return 0
    else:
        result0[n] = fibonacci0(n-1)+fibonacci0(n-2)
        return result0[n]
fibonacci0(max(arr))
fibonacci1(max(arr))
for i in arr:
    print(result0[i], result1[i])

