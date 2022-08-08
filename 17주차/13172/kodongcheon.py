x, y = input().split()

min_A = 0
min_B = 0

for i in x:
    if ord(i) <= 57:
        min_A = max(min_A, ord(i)-48)
    else:
        min_A = max(min_A, ord(i)-87)
for i in y:
    if ord(i) <= 57:
        min_B = max(min_B, ord(i)-48)
    else:
        min_B = max(min_B, ord(i)-87)
result = []
min_A = max(min_A+1, 2)
min_B = max(min_B+1, 2)
for i in range(min_A, 37):
    for j in range(min_B, 37):
        if i == j:
            continue
        if int(x, i) == int(y, j):
            result.append([int(x,i), i, j])
if len(result) == 1:
    for i in result:
        for j in i:
            print(j, end= " ")
elif not result:
    print("Impossible")
else:
    print("Multiple")

