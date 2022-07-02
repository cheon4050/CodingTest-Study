T = int(input())
for _ in range(T): # 테스트 케이스
    col = int(input())
    array = [list(map(int,input().split())), list(map(int,input().split()))]
    score = []
    score.append([0,0,0]) # 초기값
    for i in range(col):
        score_i = [0,0,0] # 한 열에 대해 각각 위쪽 스티커, 아래쪽 스티커, 선택 안함에 대응하는 최대점수
        upper, lower = array[0][i], array[1][i]
        score_i[0] = upper + max(score[i][1],score[i][2]) # upper 선택 > 이전단계의 lower, nothing 중 최댓값에 더함
        score_i[1] = lower + max(score[i][0],score[i][2])
        score_i[2] = max(score[i])
        score.append(score_i)
    print(max(score.pop()))