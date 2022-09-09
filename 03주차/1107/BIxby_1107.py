n=int(input())
m=int(input())
buttons=set(range(10))
if m>0:
    buttons-=set(map(int,input().split()))
min_cnt=abs(n-100)
for channel in range(1000000):
    for i in range(len(str(channel))):
        if int(str(channel)[i]) not in buttons:
            break
        elif len(str(channel))-1==i:
            min_cnt=min(min_cnt,abs(channel-n)+len(str(channel)))
print(min_cnt)