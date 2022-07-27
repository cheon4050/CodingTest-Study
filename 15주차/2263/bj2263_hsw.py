import sys
sys.setrecursionlimit(10 ** 6)

def implement_preorder(start_i: int, end_i: int, start_p: int, end_p: int) -> None:
    if start_i > end_i:
        return
    preorder.append(postorder[end_p])
    pivot = table[postorder[end_p]]
    implement_preorder(start_i, pivot - 1, start_p, start_p + pivot - start_i - 1)
    implement_preorder(pivot + 1, end_i, start_p + pivot - start_i, end_p - 1)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
preorder = []
table = dict()
for i, num in enumerate(inorder):
    table[num] = i
implement_preorder(0, n - 1, 0, n - 1)
print(*preorder)