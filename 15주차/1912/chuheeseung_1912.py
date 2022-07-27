import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
answer = [0] * n
answer[0] = array[0]

for i in range(1, n):
    answer[i] = max(array[i], array[i] + answer[i-1])
    # 자기 자신, 자기자신+앞의수 두개중 큰 것을 배열에 넣음
    # 바로 앞의 원소와의 합만 확인하면 된다! 음수가 있으면 최댓값이 안되니까

print(max(answer))