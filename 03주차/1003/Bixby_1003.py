for _ in range(int(input())):
    zero,one=1,0
    for i in range(int(input())):
        zero,one=one,zero+one
    print(zero,one)