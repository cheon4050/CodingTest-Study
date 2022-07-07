n = int(input())
node = [0 for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

q = [1]
node[1] = 1
while q:
    cur = q.pop()

    for i in tree[cur]:
        if node[i] == 0: #방문하지 않은 경우
            node[i] = cur
            q.append(i)

for i in range(2, n+1):
    print(node[i])