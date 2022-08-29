import heapq

N, M = map(int, input().split())

Nroot = [i for i in range(N+1)]
Elist = []
for i in range(M):
    Elist.append(list(map(int, input().split())))
Elist.sort(key=lambda x: x[2])

def find(x):
    if Nroot[x] != x:
        Nroot[x] = find(Nroot[x])
    return Nroot[x]

result = 0
wList = []

for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)

    if sRoot != eRoot:
        if sRoot > eRoot:
            Nroot[sRoot] = eRoot
        else:
            Nroot[eRoot] = sRoot

        result += w
        heapq.heappush(wList, (-w, w))

print(result - heapq.heappop(wList)[1])