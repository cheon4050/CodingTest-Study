def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(int(n)**0.5) + 1):
        if int(n) % i == 0:
            return False
    return True

def convert(n,base):
    rev_base=[]
    while n>0:
        n,mod = divmod(n,base)
        rev_base+=str(mod)
    return ''.join(rev_base[::-1])


def solution(n,k):
    cnt=0
    li=convert(n,k).split('0')
    for l in li:
        if l:
            cnt+=isPrime(int(l))
    return cnt

#print(solution(437674,3))
print(solution(110011,10))