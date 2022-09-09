n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# paper = []
# for _ in range(n):
#     row = list(map(int, input().rsplit()))
#     paper.append(row)

minus = 0
zero = 0
plus = 0

def cut(x, y, n):
    global minus, zero, plus
    check = paper[x][y]

    for i in range(x, x + n): # 종이를 돌면서
        for j in range(y, y + n):
            if(paper[x][y] != check): # 중간에 check랑 값이 다르면 종이를 9등분
                new = n // 3
                for k in range(3):
                     for l in range(3):
                        cut(x + k*new, y + l*new, new)
                return

    if(check == -1): # 종이 숫자가 모두 같으면 각각에 1 더해줌
       minus += 1
    elif(check == 0):
        zero += 1
    elif(check == 1):
        plus += 1


cut(0, 0, n)
# print(minus)
# print(zero)
# print(plus)
print(f'{minus}\n{zero}\n{plus}')
