n = int(input())
eggs = []
answer = 0
s, w = 0, 1 # s : 내구도, w : 무게

for _ in range(n):
    eggs.append(list(map(int, input().split())))

def crash(index): # index : 현재 들고 있는 계란의 인덱스
    global answer

    if index == n: # 종료 조건 : 가장 오른쪽 계란을 치고 난 뒤
        count = 0

        for i in range(n):
            if eggs[i][s] <= 0:
                count += 1 # 깨진 계란 개수 갱신

        answer = max(answer, count) # 최댓값 갱신
        return

    if eggs[index][s] <= 0: # 현재 들고 있는 계란이 깨진 경우
        crash(index + 1) # 다음 계란으로 넘어간다
        return

    isAllBroken = True
    for targetIndex in range(n):
        if targetIndex == index: # 현재 계란은 넘어간다
            continue
        if eggs[targetIndex][s] > 0: # 내구도가 0보다 크면 아직 깰 계란이 남아있다는 뜻
            isAllBroken = False # isAllBroken을 False로 바꿔준다
            break

    if isAllBroken: # 모든 계란이 다 깨져 있는 경우
        answer = max(answer, n - 1) # answer 값 갱신
        return

    for targetIndex in range(n): # 계란 때리기
        if targetIndex == index: # 현재 계란은 넘어간다
            continue

        if eggs[targetIndex][s] <= 0: # 내구도가 0보다 작으면 깨져있다는 거니까 넘어간다
            continue

        eggs[index][s] -= eggs[targetIndex][w] # 때리기
        eggs[targetIndex][s] -= eggs[index][w] # 계란의 내구도는 상대 무게만큼 깎인다
        crash(index + 1)
        eggs[index][s] += eggs[targetIndex][w] # 때린거 복구
        eggs[targetIndex][s] += eggs[index][w]

crash(0)
print(answer)