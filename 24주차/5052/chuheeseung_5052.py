def check():
    for i in range(len(phoneNum) - 1):
        # 정렬하고 나서 비교하니까 앞뒤 숫자만 비교해도 된다
        if phoneNum[i] == phoneNum[i + 1][0:len(phoneNum[i])]:
            print("NO")
            return
    print("YES")

t = int(input())

for _ in range(t):
    n = int(input())
    phoneNum = []

    for i in range(n):
        phoneNum.append(input().strip())

    phoneNum.sort()
    check()