import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

answer = 0

x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))

mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)
ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)

if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0: # 평행
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
        answer = 1
else: # 교차
    if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
        answer = 1
# 선분이 교차하거나 평행하는 경우 answer = 1
# 아니면 answer = 0

print(answer)

'''
ccw 알고리즘 : 세 점의 위치관계 파악 (벡터 외적)
- p1, p2, p3의 좌표 -> D값 리턴
- D의 경우의 수
    D > 0 : 반시계방향
    D = 0 : 평행
    D < 0 : 시계방향
'''
