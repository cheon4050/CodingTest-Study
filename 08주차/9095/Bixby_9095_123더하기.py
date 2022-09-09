for _ in range(int(input())):
    d=[1,2,4]
    for i in range(3,n:=int(input())):
        d.append(d[i-3]+d[i-2]+d[i-1])
    print(d[n-1])