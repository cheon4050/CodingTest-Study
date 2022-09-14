def calw(x1, y1, x2,y2, x3, y3):
    temp=x1*y2+x2*y3+x3*y1-(y1*x2 + y2*x3+y3*x1)
    return temp

N=int(input())
x=[0]*3
y=[0]*3

x[2],y[2]=map(int, input().split())
x[0],y[0]=map(int, input().split())
arr = [[]]*N

i=2
k=1
area=0
while(1):
    if(i>=N) :
        break # 세 점으로 나오지 않을 때
    x[k],y[k]=map(int, input().split())
    area+=calw(x[2], y[2], x[(k+1)%2], y[(k+1)%2],x[k], y[k])/2.0
    k=(k+1)%2
    i+=1
if(area>=0):
    print(round(area, 1))
else:
    print(round((-1.0)*area, 1))


'''

각 꼭지점의 x 좌표에 다음 꼭지점의 y 좌표를 곱합니다. 결과를 추가하십시오. 이 제품의 추가 합계는 82입니다.

각 꼭지점의 y 좌표에 다음 꼭지점의 x 좌표를 곱합니다. 다시이 결과를 추가하십시오. 이 제품의 추가 합계는 -38입니다.

'''