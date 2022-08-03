import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def postorder(start, end):
    if start > end:
        return
    mid = end+1
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            mid = i
            break

    postorder(start+1, mid-1)
    postorder(mid, end)
    print(tree[start])


tree = []
while True:
    try:
        node = int(input())
        tree.append(node)
    except:
        break

postorder(0, len(tree)-1)
