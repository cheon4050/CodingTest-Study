import sys
input = sys.stdin.readline
arr = {}
sum = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    sum += 1
    if tree in arr:
        arr[tree] +=1
    else:
        arr[tree] = 1
arr_keys = list(arr.keys())
arr_keys.sort()
for i in arr_keys:
    print(i + ' %.4f' %(arr[i]*100/sum))
