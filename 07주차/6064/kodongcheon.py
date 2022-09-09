import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, x, y = map(int,input().rstrip().split())

    temp = M-N
    for i in range(40000):
        temp2 = (x+i*temp)%N
        if temp2 == 0:
            temp2 = N
        if temp2 == y:
            print(x + M*i)
            break
    else:
        print(-1)