n,m = map(int, input().split())

def gcd(n, m):
    while m > 0:
        n, m = m, n % m #유클리드 호제법
    return n

def lcm(n, m):
    return n * m // gcd(n, m)

print(gcd(n, m))
print(lcm(n, m))


# 두 자연수 a,b에 대하여 a를 b로 나눈 나머지
# r에 대해 a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 이를 계속 반복하며 b가 0이 될 때, a값이 바로 최대공약수

#입력값인 두 정수 a,b에 대하여  a = x * gcd ,
# b = y * gcd (단, gcd는 a와 b의 최대공약수이고, x와 y는 서로 서로소 관계이다.) 이므로
# 최소공배수는 a*b//gcd가 된다