import sys
input = sys.stdin.readline

n = int(input()) # 문제의 개수
string = input() # 문자열

colors = {'B' : 0, 'R' : 0} # 칠할 횟수를 저장하는 딕셔너리에 초기값 0으로 저장
colors[string[0]] += 1 # 처음 색깔 칠하기

for i in range(1, n): # 다른 색이 나오면 해당 색깔을 칠하는 횟수 + 1
    if string[i] != string[i-1]:
        colors[string[i]] += 1

result = min(colors['B'], colors['R']) + 1
# 칠할 횟수가 더 많은 것을 먼저 전체에 칠하고(+1)
# 칠할 횟수가 더 적은 것의 횟수값(min)을 더한다

print(result)
