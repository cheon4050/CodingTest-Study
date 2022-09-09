import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    clothes = {}

    n = int(input())
    for _ in range(n):
        value, key = input().split()

        if clothes.get(key) == None: # 딕셔너리에 의류 종류가 없으면 새로 넣어주고
            clothes[key] = set()
        clothes[key].add(value) # 딕셔너리에 의류 종류가 있으면 원래 있는 k에 v 추가해주기

    count = 1

    for key in clothes.keys():
        count *= len(clothes[key]) + 1

    print(count - 1)

# 아무 의류도 없으면 count = 0, 의류 종류수가 1이라면 그 의류수 만큼이 답
# 의류 종류가 2개 이상이면
# (어떤 의류 종류의 의류 개수 + 1)을 모든 종류에 대해서 서로 곱해주고 1을 빼준다
# + 1 하는 이유는 그 종류의 의류를 입지 않는 경우를 포함하는 것
# 다 계산하고 마지막에 - 1 하는 이유는 모든 의류를 하나도 입지 않는 경우를 제외하는 것