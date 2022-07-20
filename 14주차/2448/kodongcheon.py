N = int(input())

def recursion(arr, n):
    global N
    for i in range(n):
        arr.append(arr[i] + " "*(n*2-1-(i*2)) + arr[i])
    if n*2 != N:
        recursion(arr, n*2)
arr = ["*", "* *", "*****"]
if N != 3:
    recursion(arr, 3)
for i in range(len(arr)):
    print(" "*(N-i-1)+arr[i]+" "*(N-i-1))