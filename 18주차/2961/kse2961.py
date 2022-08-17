#도영이가 만든 맛있는 음식
#신맛 S와 쓴맛 B
from itertools import combinations
N = int(input())
foods = [list(map(int,input().split())) for _ in range(N)]
answer = int(1e9)
for i in range(1,N+1):
    for c in combinations(range(N),i):
        s = 1
        b = 0
        for a in c:
            s*=foods[a][0]
            b+=foods[a][1]
        answer = min(answer,abs(s-b))
print(answer)