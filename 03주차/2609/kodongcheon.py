A, B = map(int,input().split())

num1 = 1
for i in range(1, min(A,B)+1):
    if A%i == 0 and B % i == 0:
        num1 = i
tempA = A
tempB = B
while(tempA != tempB):
    if tempA>tempB:
        tempB += B
    else:
        tempA += A
print(num1)
print(tempA)

# import math // lcm함수는 3.9버전 부터 추가
# print(math.gcd(A,B))
# print(math.lcm(A,B))
