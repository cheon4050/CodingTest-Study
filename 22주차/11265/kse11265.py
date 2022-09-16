n, m = map(int, input().split())
partys = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j : #
                continue
            partys[i][j] = min(partys[i][j], partys[i][k]+partys[k][j])

for _ in range(m):
    start, end, cost = map(int, input().split()) #파티장의 정보 list
    result = partys[start-1][end-1] #그 파티의 시작과 끝의 연결 result
    if cost >= result: # 그 연결 값이 cost 보다 작거나 같으면 Enjoy other party
        print("Enjoy other party")
    else:
        print("Stay here")