import math

def solution(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev=str(rev_base[::-1])
    print(rev)
    count = 0
    check = True
    for num in rev.split('0'):
        if num != '' and num != '1': #빈값이 아니고 1이 아닐 때
            num = int(num)
            #소수인지 검사
            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0: #나누어떨어지는 수가 있으면
                    check = False #소수가 아님
                    break
            if check: #check가 True라면
                count +=1 #소수니까 +1
    return count

print(solution(437674, 3))