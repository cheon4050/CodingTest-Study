import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums += list(map(int, input().split())) # 리스트에 숫자들 저장
    nums.sort(reverse=True) # 내림차순으로 정렬
    nums = nums[:n] # 입력받을 때 마다 큰 순서대로 n개만 저장
    # 다 저장하면 시간초과

print(nums[-1])