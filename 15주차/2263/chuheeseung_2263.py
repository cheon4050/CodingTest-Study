import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def preorder(in_start, in_end, post_start, post_end):
    if(in_start > in_end) or (post_start > post_end): # 종료 조건
        return

    parents = postorder[post_end] # 후위순회는 루트가 가장 마지막에 나타남
    print(parents, end=" ")

    left = position[parents] - in_start # 루트를 기준으로 범위를 나눔
    right = in_end - position[parents]

    # 범위를 좁혀서 왼쪽, 오른쪽 각각 서브트리로 재귀방식으으로 전위순회
    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)


n = int(input())
inorder = list(map(int, input().split())) # 중위순회
postorder = list(map(int, input().split())) # 후위순회

# 후위순회의 끝값이 중위순회의 어디 인덱스에 위치하는지 확인해야 함
position = [0] * (n + 1)
for i in range(n): # 중위순회 값들의 인덱스를 position 리스트에 저장
    position[inorder[i]] = i

preorder(0, n-1, 0, n-1) # 중위, 후위순회 모두 0 ~ n-1 전체 범위를 주고 전위순회를 구함
