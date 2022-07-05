n = int(input())
array = list(map(int, input().split()))
reverse_case = array[::-1]

increase = [1 for i in range(n)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(n)] # 가장 긴 감소하는 부분 수열
result = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] - 1

print(max(result))

# 각 인덱스별로 증가하는 수열 길이 + 감소하는 수열 길이 합이 가장 큰 지점 -> Sk 원소
