T = int(input())

len_A = int(input())
A = list(map(int, input().split()))

len_B = int(input())
B = list(map(int, input().split()))

answer = 0

# A 배열의 가능한 부분합 경우의 수
for i in range(len_A):
    for j in range(i, len_A):
        # A 배열의 부분합 계산
        T_A = 0
        for ind in range(i, j + 1):
            T_A += A[ind]

        # B 배열의 가능한 부분합 경우의 수
        for k in range(len_B):
            for l in range(k, len_B):
                # B 배열의 부분합 계산
                T_B = 0
                for ind in range(k, l + 1):
                    T_B += B[ind]

                # 두 배열의 부분합을 더한 결과가 T인 경우 카운팅
                if T_A + T_B == T:
                    answer += 1

print(answer)