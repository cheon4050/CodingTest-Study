n = int(input())
square_list = [0] * (n+1)
square_list[0], square_list[1] = 0, 1

for i in range(2, n + 1):
    j = 1
    minValue = 4 # 최대 개수가 4개 -> 더 작은 개수로 만들 수 있는지 밑에서 min으로 비교

    while ((j ** 2) <= i):
        minValue = min(minValue, square_list[i - (j ** 2)])
        # 더 작은 개수로 만들 수 있으면 minValue에 그 값을 넣어준다
        # n보다 작거나 같은 제곱수를 찾고 (n-제곱수)를 인덱스로 가진 값에 1을 더해준다
        j += 1

    square_list[i] = minValue + 1

print(square_list[n])