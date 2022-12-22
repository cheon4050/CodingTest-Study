R, C, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
#이동방향 1: 위 , 2: 아해, 3 : 오른쪽, 4: 왼쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

answer = 0
def checkWall(x, y): #벽인징 아닌지 확인
    if x < 1 or x > R or y < 1 or y > C:
        return True
    return False


def moving():
    global arr

    for shark in arr:
        r, c, s, d, z = shark[0], shark[1], shark[2], shark[3], shark[4] #x좌표,y좌표, 속력, 방향, 크기

        for move in range(s):
            tempR, tempC = r + dx[d], c + dy[d] # 이동하기
            if checkWall(tempR, tempC): #벽이면 방향 바꿔주기
                if d == 1: d=2
                elif d == 2: d=1
                elif d == 3: d=4
                elif d== 4: d=3

            r, c = r + dx[d], c + dy[d] #벽이었으면 바뀐 쪽으로 좌표 다시 설정

        shark[0], shark[1], shark[3] = r, c, d # 바뀐 좌표와 방향 넣어주기
    arr = sorted(arr, key=lambda x: (x[0], x[1], -x[4])) # 위치가 가장 가깝고 크기가 가장 큰거를 잡아야하기 때문ㅇ ㅔ정렬해주기
    print("정렬후 ",arr)

    temp = 0

    while temp != len(arr) - 1 and len(arr) > 0: #
        next = temp + 1
        if next >= len(arr):
            break

        if arr[temp][0] == arr[next][0] and arr[temp][1] == arr[next][1]:
            arr.pop(next)
        else:
            temp += 1

for i in range(1, C + 1):
    #일단 낚시할 수 있으면 낚시 해야하니까 fishing 하기
    top = R * 2 #8
    flag = -1

    for j, shark in enumerate(arr):
        x, y = shark[0], shark[1] #좌표

        if i == y: # 만약 낚시꾼 위치 열에 상어 위치로 해당하면
            if x < top:
                top = x #해당 위치를 top으로 설정
                flag = j # flag에 +1씩 (인덱스 값땜시)

    if flag != -1:
        answer += arr[flag][4] #잡은거니까 상어크기 추가하기
        arr.pop(flag) # 그 상어는 없애버리기
    moving() # 움직이기 (1초)

print(answer)

