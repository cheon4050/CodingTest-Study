N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
# 인덱스상 더하기 위하여 맨 앞에 0추가

for i in range(len(numbers)-1):
    # 누적 합으로 구해진 값을 저장한다
    numbers[i+1] = numbers[i+1] + numbers[i]

for _ in range(M):
    i, j = map(int, input().split())
    # i ~ j번째 까지의 합이므로 j번째가 1~j번째까지의합이고 인덱스상 i-1번째를 빼주어야 i~ j번 사이의 구간 합을 구할 수 있다.
    print(numbers[j] - numbers[i-1])