N = int(input())

for i in range(N):
    sum = i
    numlist = list(str(i))
    for num in numlist:
        sum += int(num)
    if sum == N:
        print(i)
        break
else:
    print(0)