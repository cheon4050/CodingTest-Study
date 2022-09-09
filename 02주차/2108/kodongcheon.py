import sys
from collections import Counter
sysinput = sys.stdin.readline

N = int(sysinput())
numarr = []
for i in range(N):
    num = int(sysinput())
    numarr.append(num)
numarr.sort()
average = (sum(numarr)/N)
if abs(average-int(average)) >= 0.5 : # 산술 평균
    if average < 0:
        print(int(average)-1)
    else:
        print(int(average)+1)
else:
    print(int(average))
print(numarr[N//2]) # 중앙값
counterArr = Counter(numarr).most_common()
if len(counterArr) != 1 and counterArr[0][1] == counterArr[1][1]: #최빈 값
    print(counterArr[1][0])
else:
    print(counterArr[0][0])
print(numarr[-1]-numarr[0]) # 범위