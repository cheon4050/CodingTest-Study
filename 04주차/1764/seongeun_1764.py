N, M = map(int, input().split())
#교집합을 찾는 문제
nosee=set()
nolisten=set()
#rstrip : 인자로 전달된 문자를 String의 오른쪽에서 제거
for i in range(N):
    nosee.add(input().rstrip())
for i in range(M):
    nolisten.add(input().rstrip())

result=sorted(list(nosee&nolisten))
print(len(result))
for i in result:
    print(i)