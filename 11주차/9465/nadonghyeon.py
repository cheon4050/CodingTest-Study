T = int(input())
for i in range(T):
    s = []
    n = int(input())
    for a in range(2):
        s.append(list(map(int, input().split())))
    for k in range(1,n):
        if k == 1:
            s[0][k] += s[1][k-1]
            s[1][k] += s[0][k-1]
        else:
            s[0][k] += max(s[1][k-1], s[1][k-2])
            s[1][k] += max(s[0][k-1], s[0][k-2])
    print(max(s[0][n-1], s[1][n-1]))

