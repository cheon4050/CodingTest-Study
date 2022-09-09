n = int(input())
dp_list = [0 for _ in range(n + 1)] # dp_list를 0으로 초기화

for i in range(2, n + 1):
    dp_list[i] = dp_list[i-1] + 1 # 먼저 1을 뺀 경우의 수 저장

    # 2로 나누어질 경우 기존 1을 뺀 경우의 수랑 비교해서 최솟값을 저장
    if i % 2 == 0:
        dp_list[i] = min(dp_list[i], dp_list[i//2] + 1)

    # 3으로 나누어질 경우 기존 1을 뺀 경우의 수랑 비교해서 최솟값을 저장
    # 2 또는 3으로 나누어질 경우에 모든 경우를 비교해야 해서 eilf가 아니라 if
    if i % 3 == 0:
        dp_list[i] = min(dp_list[i], dp_list[i//3] + 1)

print(dp_list[n])