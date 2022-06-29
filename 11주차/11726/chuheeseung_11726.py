n = int(input())
y = [0] * (n + 1)

if n <= 3:
    print(n)
else:
    y[1] = 1 # n = 1인 경우 1가지
    y[2] = 2 # n = 2인 경우 2가지

    for i in range(3, n + 1):
        y[i] = y[i-1] + y[i-2]
        # n = 3인 경우 = n = 1인 경우 + n = 2인 경우

    print(y[i] % 10007)