import sys
sys.setrecursionlimit(10**5)
# 재귀 형태로 트리 순회(후위)
def recursive(left, right):
    # 범위를 벗어나게 되면 반환(돌아야 할 값이 없음(
    if left > right:
        return
    # 루트 값을 기준으로 오른쪽 서브트리인지 확인한다.
    root = tree[left]
    idx = left + 1 # 각 서브트리의 끝을 모르기 때문에 구해야한다(left + 1부터)
    # 서브트리 크기의 끝까지 검색
    while idx <= right:
        # 루트보다 값이 크면 해당 값부터 오른쪽 서브트리를 의미
        if root < tree[idx]:
            break
        idx += 1
    # 왼쪽, 오른쪽 서브트리 탐색 후 결과 값을 출력하는 방식이 후위 순회
    recursive(left + 1, idx - 1)
    recursive(idx, right)
    print(root)


# 전위 순회한 결과를 받았을 때 후위 순회한 결과로 반환하기
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break
recursive(0, len(tree) - 1)