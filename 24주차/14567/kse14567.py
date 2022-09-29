'''
모든 전공 과목을 다 들으려는 목적
선수과목 조건을 지킬 경우 각각의 전공과목을 언제 이수 할 수 있는지

1. 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
2. 모든 과목은 매 학기 항상 개설 됨.

모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기?
'''

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
temp = [0] + [1 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a) #A, B 구조 만들어주고

for i in range(1, n+1):
    for sub in graph[i]:
        print(graph[i],"번째, ",temp[i], temp[sub]+1)
        temp[i] = max(temp[i], temp[sub]+1)
        print(temp[i])
#temp[2] = 2 -> temp[3]=2 -> temp[5]=3 -> 3
for j in range(1, n+1):
    print(temp[j], end=' ')