for _ in range(int(input())):
    m,n,x,y=map(int,input().split())
    while x<=m*n:
        if (x-y)%n==0:
            print(x)
            break
        x+=m
    else:
        print(-1)