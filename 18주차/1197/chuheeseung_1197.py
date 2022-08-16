import sys
input = sys.stdin.readline

v, e = map(int, input().split()) # 정점의 개수 v, 간선의 개수 e
v_root = [i for i in range(v + 1)] # 루트를 저장하는 배열
e_list = []

for _ in range(e):
    e_list.append(list(map(int, input().split())))

e_list.sort(key = lambda x : x[2]) # 간선 리스트를 가중치 기준으로 정렬

def find(a):
    if a != v_root[a]:
        v_root[a] = find(v_root[a])

    return v_root[a]

sum = 0

for s, e, w in e_list:
    s_root = find(s) # 간선들이 이은 정점을 find 함수로 찾음
    e_root = find(e)

    if s_root != e_root: # 루트값이 다르면 큰 값을 작은 값으로 만들어서 연결되게 해준다
        if s_root > e_root:
            v_root[s_root] = e_root
        else:
            v_root[e_root] = s_root

        sum += w # 가중치를 더해준다

print(sum)
