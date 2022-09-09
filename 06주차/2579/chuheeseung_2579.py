import sys
input = sys.stdin.readline

n = int(input())
count = [0 for _ in range(n + 3)] # 계단 i칸까지 오를 때의 최댓값
stairs = [0 for _ in range(n + 3)] # 입력한 해당 계단의 숫자

for k in range(1, n + 1):
    stairs[k] = int(input())

count[1] = stairs[1] # 계단 1칸 올랐을 때
count[2] = stairs[1] + stairs[2] # 계단 2칸 올랐을 때
count[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]) # 계단 3칸 올랐을 때

for i in range(4, n + 1):
    count[i] = max(count[i-3] + stairs[i-1] + stairs[i], count[i-2] + stairs[i])

print(count[n])

# 4칸 부터 고려해야 할 것들 (3칸 연속되는 계단을 밟을 수 없어서)
# 1. count[i] = count[i-2] + stairs[i]
#   i칸을 밟기 전의 칸이 i-2칸 -> 3칸 연속 밟을 일 없음
# 2. count [i] = count[i-1] + stairs[i]
#   i칸 이전에 i-1칸을 밟아서 3칸 연속일 수 있음 -> 한칸 전의 count말고 3칸 전의 count로 이동해야함
#   -> 고치면 count[i] = count[i-3] + stairs[i-1] + stairs[i]
# => 최종 점화식 : 1과 2중 최댓값