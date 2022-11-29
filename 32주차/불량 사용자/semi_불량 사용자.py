# 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return

import re
from collections import defaultdict

paths = list()              # 중복 제거 전의 모든 가능한 경로를 담는 리스트
def dfs(depth, banned_dic, path):
    if depth == len(banned_dic):    # depth : 불량 사용자 아이디 인덱스
        paths.append(path)
        return

    for i in range(len(banned_dic[depth])):
        if banned_dic[depth][i] in path:   # 응모자 아이디가 중복해서 제재 아이디 목록에 들어갈 수 없으므로 이미 앞선 탐색 경로에 있는 아이디라면 백트래킹
            continue

        path.append(banned_dic[depth][i])   # 탐색 경로에 사용자 아이디 추가
        dfs(depth + 1, banned_dic, path[:])   # path[:] : 배열의 참조가 아닌 복사 후 재구 함수 인자로 전달
        path.pop()


def solution(user_id, banned_id):  # 응모자 아이디 목록, 불량 사용자 아이디 목록
    banned_dic = defaultdict(list)
    for idx, ban in enumerate(banned_id):     # 각 불량 사용자 아이디와 일치하는 응모자 아이디 구하기
        p = re.compile(ban.replace("*", "."))
        for user in user_id:
            if p.match(user) and len(user) == len(ban):
                banned_dic[idx].append(user)    # 같은 불량 사용자 아이디 목록이 존재하므로 딕셔너리 키로 인덱스를 사용

    dfs(0, banned_dic, [])
    return len(set([tuple(sorted(path)) for path in paths]))

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))