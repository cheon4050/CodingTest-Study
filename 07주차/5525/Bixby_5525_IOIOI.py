n=int(input())
m=int(input())
s=input()
cntIO=0
cntPn=0
step=0
while step<(m-1):
    if s[step:step+3]=="IOI":
        cntIO+=1
        step+=2
        if cntIO==n:
            cntIO-=1
            cntPn+=1
    else:
        step+=1
        cntIO=0
print(cntPn)