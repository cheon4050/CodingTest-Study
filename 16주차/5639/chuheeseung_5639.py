import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def post_order(start, end):
    if start > end: # 시작 인덱스가 끝 인덱스를 넘어간 경우 리턴
        return

    root = pre_order[start] # 루트 노드
    idx = start + 1

    while idx <= end: # 루트보다 큰 지점을 찾아서 idx에 저장
        if pre_order[idx] > root: 
            break
        idx += 1

    post_order(start + 1, idx - 1) # 왼쪽 서브트리 
    post_order(idx, end) # 오른쪽 서브트리

    print(root)

pre_order = []

while 1:
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(0, len(pre_order) - 1)

# 전위순회 : 루트 -> 왼쪽, 오른쪽 재귀 호출
# 후위순회 : 왼쪽, 오른쪽 재귀 호출 -> 루트