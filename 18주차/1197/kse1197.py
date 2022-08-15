#최소 스패닝 트리
#python3 시간초과/pypy3 통과
V,E=map(int,input().split())
edge_list = []
root=[i for i in range(V+1)]
for _ in range(E):
    pre,post,C=map(int, input().split())
    edge_list.append((C, pre, post))
edge_list.sort() # 가중치 기준으로 오름차순 정렬
# print(edge_list)

def checkRoot(n):
    if n != root[n]:
        root[n] = checkRoot(root[n])
    return root[n]
answer = 0
for c, pre, post in edge_list:
    pre_root = checkRoot(pre)
    post_root = checkRoot(post)
    # 두 정점의 root가 다르다면 하나의 루트로 연결
    if pre_root != post_root:
        if pre_root > post_root:
            root[pre_root] = post_root
        else:
            root[post_root] = pre_root
        answer += c
    # print(root)
print(answer)