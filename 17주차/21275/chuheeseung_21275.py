import sys
input = sys.stdin.readline

A, B = input().split()
x, a, b = 0, 0, 0
count = 0

for i in range(2, 37): # 35까지 표현할 수 있다 = 36진수
    try:
        a_temp = int(A, i) # A라는 값을 i진수로 변환
    except:
        continue

    for j in range(2, 37):
        try:
            b_temp = int(B, j)

            if a_temp == b_temp: # 진수 변환한 값이 같으면 count +1, a, b 값 넣어줌
                count += 1
                a = i
                b = j
        except:
            continue

if count == 1: # 1개인 경우
    print(x, a, b)
elif count == 0:
    print("Impossible")
else:
    print("Multiple")