t = int(input())

for _ in range(t):
    p_list = [0, 1, 1, 1, 2, 2] # 0부터 시작하는 거로 생각해야 한다!

    n = int(input())

    for i in range(6, n + 1):
        p_list.append(p_list[i - 1] + p_list[i - 5])

    print(p_list[n])

# 새로 만들어지는 삼각형의 한 변의 길이 = 그 전의 삼각형 변의 길이 + 5번째 전에 만들었던 삼각형 변의 길이