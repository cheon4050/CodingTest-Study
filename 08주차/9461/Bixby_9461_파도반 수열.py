for _ in range(int(input())):
    d=[1,1,1,2,2]
    n=int(input())
    for i in range(5,n):
        d.append(d[i-5]+d[i-1])
    print(d[n-1])