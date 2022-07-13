A,B = map(int, input().split())

count = 1
#B에서 A로 가는 방법 이용
while True:
    #A와 B가 같아지면 while을 break한다
    if A == B:
        break
    #B를 2로 나눈 나머지가 0이 아니고 B의 마지막 자리가 1이 아니거나 A가 B보다 크면 값을 만들 수 없다. 그래서 -1을 출력한다.
    elif (B % 2 != 0 and B % 10 != 1) or (A > B):
        count = -1
        break
    else:
        #B의 마지막 자리가 1이면 B에서 1을 제거한다.
        if B % 10 == 1:
            B //= 10
            count += 1
        else:
            #B가 2로 나누어 떨어지면 2로 나눈다.
            B //= 2
            count += 1

print(count)