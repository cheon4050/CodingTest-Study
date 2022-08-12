days = [0] * 366  # 365일 배열

import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
  S, E = map(int, input().split())  # 시작일, 끝일 받아오기
  for se in range(S, E+1):
    days[se] += 1  #  일정있는 일에 1개씩 늘이기

row = 0
col = 0
ans = 0

for d in range(1, 366):
  if days[d]:
    row = max(row, days[d])
    col += 1
  else:
    ans += row * col
    row = 0
    col = 0
ans += row * col  # 365일에 해당하는 부분도 고려

print(ans)