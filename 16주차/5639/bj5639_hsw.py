import sys
sys.setrecursionlimit(10 ** 6)

def preorder_to_postorder(start, end) -> None:
    if start > end:
        return
    pivot = start
    for i in range(start + 1, end + 1):
        if preorder[i] > preorder[pivot]:
            pivot = i - 1
            break
    preorder_to_postorder(start + 1, pivot)
    preorder_to_postorder(pivot + 1, end)
    print(preorder[start])

preorder = []
while True:
    num = sys.stdin.readline().rstrip()
    if not num:
        break
    preorder.append(int(num))
preorder_to_postorder(0, len(preorder) - 1)