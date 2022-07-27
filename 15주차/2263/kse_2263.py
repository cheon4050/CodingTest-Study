import sys
sys.setrecursionlimit(10 ** 6)

def divide_tree(l, r, pl, pr): # inorder의 어디부터 어디까지를 왼쪽/오른쪽 sub tree으로 볼것이며,
    # postorder의 어디부터 어디까지를 왼쪽/오른쪽 sub tree으로 볼것인지 정함

    if l > r or pl > pr:
        return

    root = postorder[pr]  # postorder에서는 항상 맨 뒤(즉 맨 오른쪽)의 index가 subtree의 root
    #print(in_l, in_r, post_l, post_r, root)  # 종결 조건이 유효한지 보자.
    print(root, end=" ")      # 뽑기
    idx_root = in_idx[root]  # root의 index를 inorder에서 찾으면

    left_cnt = idx_root-l
    right_cnt = r-idx_root

    divide_tree(l, idx_root-1,pl, pl+left_cnt-1) # pre에선 왼쪽먼저
    divide_tree(idx_root+1,r, pr-right_cnt,pr-1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# postorder를 참조하여 바꾸되, inorder를 지표삼아 좌우를 구분한다.
in_idx = [0 for _ in range(n+1)] # inorder를 지표 삼기위해 각 node가 inorder에 몇번째 index에 있는지 확인
for i in range(n):
    in_idx[inorder[i]] = i # inorder의 i번째는 n이다. <=> node n은 inorder에서 i번째 index이다. (in_idx[n]=i)

divide_tree(0, n-1, 0, n-1)