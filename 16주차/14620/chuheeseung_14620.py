def check(lists):
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, -1, 0, 1]
    checkList = []
    result = 0

    for flower in lists:
        x = flower // n # 1차원 리스트에서 x좌표, y좌표를 구함
        y = flower % n

        if x == 0 or x == n-1 or y == 0 or y == n-1: # 가장자리인 경우
            return 100000

        for i in range(5): # 꽃이 피었을 때의 좌표를 배열에 넣음
            checkList.append((x + dx[i], y + dy[i]))
            result += garden[x + dx[i]][y + dy[i]] # 비용 담는 변수에 저장

    if len(set(checkList)) == 15:# 중복을 없애기 위해 set 사용, 15개가 찬 경우
        return result

    return 100000

n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]
price = 100000

# 꽃 3개의 위치를 삼중 반복문으로 돈다
for i in range(n * n): # 2차원 리스트로 생각안하고 1차원으로 생각
    for j in range(n * n):
        for k in range(n * n):
            flowers = [i, j, k]
            price = min(price, check(flowers))

print(price)