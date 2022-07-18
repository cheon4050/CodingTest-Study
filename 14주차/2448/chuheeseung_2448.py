n = int(input())
graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]

def recursive(N, before): # before : 이전 별찍기 모양
    after = [[" "] * (2 * 2 * N - 1) for _ in range(2 * N)] # 현재 별찍기 모양 저장 리스트
    for i in range(N): # n번째줄까지는 이전 별찍기 모양을 그대로 복사
        after[i][N:N + 2*N - 1] = before[i] # 범위 외에는 공백을 지켜야함

    k = 0
    for i in range(N, 2 * N):
        after[i][:2*N] = before[k] # 이전 그래프 모양을 양 옆으로 복사
        after[i][2*N:2*N + len(before[k])] = before[k]
        k += 1

    if 2 * N == n: # n이 되면 after 리턴
        return after

    return recursive(2 * N, after) # 마지막 줄에 도착할 때까지 계속 재귀를 돈다

if n == 3: # 재귀문을 돌지 않고 바로 출력
    result = graph
else: # n=6부터 재귀문을 돈다
    result = recursive(3, graph)

for i in result:
    print("".join(i))

# n=3이 기본 -> 재귀문 돌지 않고 바로 출력
# n=6부터 재귀문 : 양 옆으로 삼각형을 복사
# 제출 성공하려면 별을 제외한 양옆의 모든 칸을 공백으로 채워야 한다