from collections import deque

def bfs(n, info):
    result = [] # result : 최대점수차를 내는 화살 상황들을 모아둔 리스트
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0 # maxGap : 어피치와 라이언의 최대점수차

    while q:
        focus, arrow = q.popleft()
        # focus : 지금 몇점에 화살을 쏠 것인지 나타냄 -> 0
        # arrow : 현재 화살 상황 -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        if sum(arrow) == n: # 종료 조건 1. 화살을 다 쏜 경우
            apeach, lion = 0, 0 # apeach : 라이언의 점수, lion : 라이언의 점수

            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i

            if apeach < lion: # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap # 최대점수차 갱신
                    result.clear()
                result.append(arrow) # 최대점수차를 내는 화살상황 저장

        elif sum(arrow) > n: # 종료 조건 2. 화살을 더 쏜 경우
            continue

        elif focus == 10: # 종료 조건 3. 화살을 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))

        else: # 화살 쏘기
            tmp = arrow.copy() # 이기는 조건 1. 어피치보다 1발 많이 쏘기
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))

            tmp2 = arrow.copy() # 이기는 조건 2. 0발을 쏴서 덱에 넣어준다
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))
    return result

def solution(n, info):
    winList = bfs(n, info) # winList : 최대점수차를 내는 화살 상황들을 모아둔 리스트를 반환받음

    if not winList:
        # 원소가 없다 = 라이언이 이기는 경우가 없다 = [-1] 리턴
        return[-1]
    elif len(winList) == 1:
        # 원소가 1개 존재 = 최대점수차를 내는 상황이 한가지 = 해당 상황 리턴
        return winList[0]
    else:
        # 원소가 여러개 존재 = 최대점수차를 내는 상황이 여러개 = 가장 낮은 점수를 더 많이 맞힌 경우를 리턴
        # focus로 높은 점수부터 화살을 쏘도록 했음 -> 더 낮은 점수를 맞힌 경우가 나중에 append됨
        # -> 가장 낮은 점수를 맞힌 경우는 winList의 마지막 원소가 된다
        # -> winLispt[-1] 리턴
        return winList[-1]


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))


# 라이언이 어피치를 이기려면
# 1. 어피치보다 1개 더 많이 쏘거나
# 2. 과녁에 아예 0발을 쏘고 화살을 아껴서 다른 과녁의 승률을 높여준다
# 두가지 경우때문에 arrow를 복사한 리스트를 두개 만들고
# 하나에는 이기는 조건 1 -> 1개 더 많이 쏘고
# 다른 하나에는 이기는 조건 2 -> 0발을 쏴서 덱에 넣어준다
# 두가지 경우로 focus번재 과녁에 화살을 쏜다
# 다음 while문에서 다음 과녁을 봐야 해서 focus + 1

# 이렇게 쏘다 보면 극단적으로 계속 어피치보다 1개 많이 쏘는 상황이 생길 수 있음
# -> 주어진 화살 개수보다 더 많이 쏘게 되는 경우를 컷한다
# 마찬가지로 계속 0발만 쏘는 상황이 생길 수 있다
# -> focus = 10이 되어 마지막 과녁을 쏠 차례까지 된 경우 남은 화살을 전부 마지막 과녁에 쏴준다
# -> 화살을 다 쐈으니까 focus는 이제 필요 없으므로 아무 값이나 넣어준다 // 종료 조건 2, 3

# 화살을 다 쏘면 점수를 계산한다
# 라이언의 점수가 높은 경우 -> 어피치와의 점수차를 계산해서 최대점수차를 갱신한다 // 종료 조건 1