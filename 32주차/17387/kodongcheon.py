x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def ccw(x1, y1, x2, y2, x3, y3):
    cnt = x1*y2 + x2*y3 + x3*y1
    cnt -= y1*x2 + y2*x3+y3*x1

    if cnt > 0:
        return 1
    elif cnt == 0:
        return 0
    else:
        return -1

x1x2 = ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)
x3x4 = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)

if x1x2 <= 0 and x3x4 <= 0:
    if x1x2 == 0 and x3x4 == 0:
        if (max(x1,x2) >= min(x3, x4) and max(x3, x4) >= min(x1,x2)) and (max(y1,y2) >= min(y3,y4) and max(y3,y4) >= min(y1,y2)):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)