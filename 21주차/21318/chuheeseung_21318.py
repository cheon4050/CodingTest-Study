import sys
input = sys.stdin.readline

n = int(input()) # 악보의 개수
play = list(map(int, input().split())) # 악보의 난이도
play = [0] + play
fail = [0] * (n + 1) # 실수한 개수 누적합

for i in range(n): # 각 인덱스 별로 실패한 횟수 계산
    if play[i] > play[i + 1]:
        fail[i] += 1

for i in range(1, len(fail)): # 실패한 횟수의 누적합을 구한다
    fail [i] += fail[i-1]

q = int(input()) # 질문의 개수

for _ in range(q): # 질문의 개수만큼 for문 반복
    x, y = map(int, input().split())
    answer = fail[y] - fail[x-1] # 누적합 활용해서 개수 계산
    if fail[y] != fail[y-1]: # 마지막곡 y 누적합과 그 전 y-1 누적합이 다르면 1 감소
        answer -= 1 # 마지막은 항상 성공하니까
    print(answer)