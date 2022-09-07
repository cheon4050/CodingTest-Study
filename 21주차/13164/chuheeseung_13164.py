import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 유치원생 수 n명, 조 k개
kids = list(map(int, input().split())) # 원생들의 키 배열
diff = [] # 인접한 원생과의 키 차이를 저장하는 리스트
sum = 0

for i in range(0, n - 1):
    diff.append(kids[i+1] - kids[i])

diff.sort()

for i in range(n - k):
    sum += diff[i]

print(sum)