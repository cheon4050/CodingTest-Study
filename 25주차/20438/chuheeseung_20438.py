import sys
input = sys.stdin.readline

# n : 학생 수
# k : 졸고 있는 학생 수
# q : 지환이가 출석 코드를 보낼 학생 수
# m : 주어질 구간의 수
n, k, q, m = map(int, input().split())
k_list = list(map(int, input().split())) # k명 입장 번호
q_list = list(map(int, input().split())) # q명 입장 번호
dp = [1] * (n + 3) # dq 리스트 1로 초기화
dp_sum = [0] * (n + 3)

while q_list:
    start = q_list.pop(0)

    if start not in k_list: # 출석하면 0으로 바꿔줌 -> 특정 구간의 범위에서 1의 개수를 구해주면 된다
        for num in range(1, ((n + 2) // start) + 1):
            if start * num not in k_list:
                dp[start * num] = 0

for num in range(3, n + 3): # 누적합 이용해서 1의 개수를 따로 저장
    if num == 3:
        dp_sum[num] = dp[num]
    else:
        dp_sum[num] = dp[num] + dp_sum[num-1]

for _ in range(m):
    i, j = map(int, input().split()) # 구간의 범위 s, e
    print(dp_sum[j] - dp_sum[i-1])
    # 부분합 이용 : S(s~e) = S(s) - S(1~(e-1))