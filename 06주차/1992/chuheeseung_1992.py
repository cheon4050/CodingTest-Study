n = int(input())
img = [list(map(int, input())) for _ in range(n)]

def quardTree(x, y, n):
    check = img[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != img[i][j]:
                check = -1
                break

    if check == -1: # 숫자 다르면 분할 
        print("(", end="") # 괄호를 일단 넣고 4개로 쪼개고 나서 마지막에 괄호를 닫아준다
        n = n // 2

        quardTree(x, y, n)
        quardTree(x, y + n, n)
        quardTree(x + n, y, n)
        quardTree(x + n, y + n, n)

        print(")", end="")

    elif check == 1: # 모두 1인 경우
        print(1, end="")

    else: # 모두 0인 경우
        print(0, end="")


quardTree(0, 0, n)