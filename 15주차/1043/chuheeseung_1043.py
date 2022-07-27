import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n : 사람의 수, m : 파티의 수
know = list(map(int, input().split()))[1:] # 거짓말을 하면 안될 사람들을 담는 스택

visit = [0] * n # 스택에 추가된 적이 있는지 확인하기 위한 리스트
for k in know:
    visit[k-1] = 1

parties = []
for _ in range(m):
    guests = list(map(int, input().split()))[1:] 
    parties.append(guests)

party_visit = [0] * m # 진실을 말해야 하는 파티일 경우 1로 표기

while know: # 스택이 빌 때 까지 과정 반복
    known_guest = know.pop() 

    candidate = set() # pop된 사라믇ㄹ과 같은 파티에 있는 사람들을 담는 집합

    for party_idx in range(len(parties)): # pop된 사람과 같은 파티에 있는 사람들을 찾아 집합에 추가
        party = set(parties[party_idx])

        if known_guest in party: # pop된 사람이 현재 파티에 있을 경우 
            candidate = candidate.union(party) # 파티의 사람들을 집합에 추가
            party_visit[party_idx] = 1 # 현재 파티를 진실을 말해야 하는 파티라고 표기

    for guest in candidate: # 찾은 사람들 중 스택에 추가된 적이 없는 사람들을 스택에 추가
        if not visit[guest - 1]:
            know.append(guest)
            visit[guest - 1] = 1

print(party_visit.count(0)) # 표기되지 않은 파티의 개수를 출력