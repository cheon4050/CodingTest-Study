n = int(input())

result = 4
sqrt = int(n**(1/2))
if sqrt**2 == n:
    print(1)
else:
    for i in range(1, sqrt+1):
        for j in range(i, sqrt+1):
            if i**2 + j**2 == n:
                result=2
    for i in range(1, sqrt+1):
        for j in range(i, sqrt+1):
            for k in range(j, sqrt+1):
                if i**2 + j**2 +k**2== n:
                    result=min(result,3)
    print(result)

