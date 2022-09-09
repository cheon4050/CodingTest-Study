n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def recursive(x, y, n):
    global white, blue
    color = paper[x][y]
    check = True

    for i in range(x, x + n):
        if not check:
            break

        for j in range(y, y + n):
            if color != paper[i][j]:
                check = False

                recursive(x, y, n//2) # 1사분면
                recursive(x, y + n//2, n//2) # 2사분면
                recursive(x + n//2, y, n//2) # 3사분면
                recursive(x + n//2, y + n//2, n//2) # 4사분면

                break

    if check:
        if color: # 파란색이 1
            blue += 1
        else: # 하얀색이 0
            white += 1

recursive(0, 0, n)
print(white)
print(blue)