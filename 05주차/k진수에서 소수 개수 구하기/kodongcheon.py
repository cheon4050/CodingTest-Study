def solution(n, k):
    nums = ''
    arr = []
    # 진수 변환
    while(n >= 1):
        nums= str(n % k)+nums
        n = n//k
    temp = ""
    # 0으로 구분해 1이 아닌 숫자 찾기
    for num in nums:
        if num == "0":
            if len(temp) == 0:
                continue
            elif temp == "1":
                temp = ""
                continue
            arr.append(int(temp))
            temp = ""
            continue
        temp += num
    if len(temp) != 0 and temp != "1":
        arr.append(int(temp))

    cnt = 0
    # 소수 찾기
    for num in arr:
        i = 2
        while(int(num**(1/2))>=i):
            if num % i == 0:
                break
            i+=1
        else:
            cnt+=1
    return cnt