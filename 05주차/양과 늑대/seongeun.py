answer = 0
l = [-1] * 20
r = [-1] * 20
visited = [0] * (1 << 17) #2의 17승 만큼의 배열

n=0
def solution(info, edges):
    global n;
    for edge in edges:
        a, b = edge
        if l[a] == -1:
            l[a] = b #키 밸류 잡아주기
        else:
            r[a] = b
    n = len(info)
    noding(1, info)
    return answer


def noding(state, info):
    global answer
    if visited[state]:
        return
    visited[state] = 1
    wolf = 0
    sheep = 0
    for i in range(n):
        if state & (1 << i):
            if info[i]:
                wolf += 1
            else:
                sheep += 1
    if wolf >= sheep:
        return
    answer = max(answer, sheep)

    for i in range(n):
        if state & (1 << i):
            if l[i] != -1:
                t = state | (1 << l[i])
                noding(t, info)
            if r[i] != -1:
                t = state | (1 << r[i])
                noding(t, info)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))