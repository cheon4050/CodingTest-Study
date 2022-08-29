def recursion(n):
    if n == 0: # n이 0인 경우 : 0 리턴
        return 0

    if n == 1: # n이 1인 경우 : 1 리턴
        return 1

    if n % 2: # n이 홀수인 경우 : 1-recursion(n//2) 재귀 호출
        return 1 - recursion(n // 2)
    else: # n이 짝수인 경우 : recursion(n//2) 재귀 호출
        return recursion(n // 2)

k = int(input())
print(recursion(k-1))