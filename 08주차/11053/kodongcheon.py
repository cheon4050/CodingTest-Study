A = int(input())

arr = list(map(int, input().split()))

length = [0] * A

for i in range(A):
    length[i] = 1;
    for j in range(i):
        if(arr[j] < arr[i]):
            length[i] = max(length[i], length[j] + 1)
            print(length)
print(max(length))