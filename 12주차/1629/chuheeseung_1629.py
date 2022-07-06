a, b, c = map(int, input().split())

def dnc(a, b):
    if b == 1:
        return a % c

    temp = dnc(a, b // 2)

    if b % 2 == 0: # b가 짝수인 경우 temp * temp
        return temp * temp % c
    else: # b가 홀수인 경우 temp * temp * a
        return temp * temp * a % c

print(dnc(a, b))

# (a * b) % m = ((a % m) * (b % m)) % m
# 정해진 값을 절반으로 나눠서 계산
# 지수가 짝수 : 2^10 = 2^5 * 2^5
# 지수가 홀수 : 2^11 = 2^5 * 2^5 * 2