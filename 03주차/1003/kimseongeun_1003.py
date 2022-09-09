N = int(input())

num0 = [1, 0]
num1 = [0, 1]

for i in range(2,41):
    num0.append(num0[i-1]+num0[i-2])
    num1.append(num1[i-1]+num1[i-2])
    # num0[i] = num0[i-2] + num0[i-1]
    # num1[i] = num1[i-2] + num1[i-1]

for j in range(N):
    num=int(input())
    print(num0[num], num1[num])

