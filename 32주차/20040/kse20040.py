#??????????
def find(number, parent):
    if(number == parent[number]):
        return number

    parent[number] = find(parent[number], parent)
    return parent[number]

def union(a, b, parent, level):
    u = find(a, parent)
    v = find(b, parent)

    if(u == v):
        return True

    if level[u] > level[v]:
        parent[u] = v
    else:
        parent[v] = u

    if(level[u] == level[v]):
        level[v] += 1

    return False

N, M = map(int, input().split())

parent = [x for x in range(N)]
level = [1 for _ in range(N)]

for count in range(M):
    a, b = map(int, input().split())
    if union(a, b, parent, level):
        print(count + 1)
        break
else:
    print(0)