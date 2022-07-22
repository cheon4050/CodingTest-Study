from collections import deque

def bfs(parties):
    q = deque(parties)
    N = len(q)
    while True:
        for _ in range(len(q)):
            party = q.popleft()
            flag = True
            for elem in party:
                if elem in truth:
                    flag = False
                    break
            if not flag:
                truth.update(party)
            else:
                q.append(party)
        # 값이 변하지 않으면 진실을 아는 자가 파티에 없는거
        if (not q) or len(q) == N:
            break
        N = len(q)
    return len(q)

truth = set()

N, M = map(int, input().split())
truth.update(input().split()[1:])
parties = [input().split()[1:] for _ in range(M)]

print(bfs(parties))