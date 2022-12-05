# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값) 구하기

def dfs(start, node, visit):
    st = [start]
    visit[start] = True
    cnt = 1       # 한 트리에 몇개가 연결되어 있는지 체크

    while st:
        x = st.pop()
        for w in node[x]:  # 인접한 노드들에 대해 아직 방문하지 않은 경우만 탐색 진행
            if not visit[w]:
                cnt += 1
                visit[w] = True
                st.append(w)
    return cnt


def solution(n, wires):
    result = float("inf")

    for i in range(len(wires)):
        node = [[] for _ in range(n + 1)]   # 인접한 노드 정보
        visit = [False for _ in range(n + 1)]  # 방문 정보

        temp_wires = wires[:]
        temp_wires.remove(wires[i])   # 전선을 하나씩 끊기

        for w in temp_wires:          # 인접한 노드 정보 초기화
            node[w[0]].append(w[1])
            node[w[1]].append(w[0])

        size1 = dfs(1, node, visit)     # 첫번째 부분 트리에 대해 개수 탐색
        size2 = 0
        for j in range(len(visit)):           # 아직 방문되지 않은 노드를 기준(다른 부분 트리)으로 다시 탐색
            if not visit[j] and j != 0:
                size2 = dfs(j, node, visit)
                break

        result = min(result, abs(size1 - size2))   # 두 분할의 차이가 가장 적은 값을 택
    return result

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))