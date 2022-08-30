n = int(input())
# n까지의 소수 구하기
primes = [True]*(n+1)
for i in range(2, int(n**0.5)+1):
    if primes[i]:
        for j in range(i+i, n+1, i):
            primes[j] = False

primes = [i for i in range(2, n + 1) if primes[i]] + [0]
# 연속합 구하기
cnt = 0
l = r = 0
sum = 2  # primes[0]
while r < len(primes)-1:
    if sum == n:
        cnt += 1
        r += 1
        sum += primes[r]
    elif sum > n:
        sum -= primes[l]
        l += 1
    else:
        r += 1
        sum += primes[r]
print(cnt)
