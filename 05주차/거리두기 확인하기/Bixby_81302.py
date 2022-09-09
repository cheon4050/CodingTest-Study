def solution(places):
    answer=[]
    for room in places:
        illigal=False

        for x in range(4):
            for y in range(4):
                squere=room[x][y:y+2]+room[x+1][y:y+2] #2X2 사각형 만들기
                if (squere.count("P")>=2) and ("O" in squere): #대각선 체크
                    illigal=True

        for x in range(5):
            if ("PP" in room[x]) or ("POP" in room[x]): #행 체크
                illigal=True
            column=''.join([room[i][x] for i in range(5)]) #열 체크
            if ("PP" in column) or ("POP" in column):
                illigal=True

        answer.append(+(not illigal))
    return answer








places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
#result = [1, 0, 1, 1, 1]
print(solution(places))