import sys
input = sys.stdin.readline

n, m = map(int, input().split())

noSee = [input().strip() for i in range(n)] # 문자열 옆에 공백이 있어서 공백 없애줘야함
noListen = [input().strip() for j in range(m)]

noSeeSet = set(noSee) # 리스트를 집합으로 변환
noListenSet = set(noListen)

intersection = sorted(list(noSeeSet & noListenSet)) # 사전순으로 출력해야 해서 정렬함

print(len(intersection))

for i in intersection:
    print(i)