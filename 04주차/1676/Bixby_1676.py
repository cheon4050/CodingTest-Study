import math
m=math.factorial(int(input()))
cnt=0
for i in str(m)[::-1]:
    if int(i):
        break
    cnt+=1
print(cnt)