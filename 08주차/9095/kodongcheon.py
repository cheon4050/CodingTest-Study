from itertools import product
T = int(input())

arr = [0] * 11
for i in range(1, 12):
    for j in product([1,2,3], repeat=i):
        a = sum(j)
        if a < 11:
            arr[a] += 1
print(arr)
for _ in range(T):
    n = int(input())
    print(arr[n])