from itertools import permutations
import re

def solution(user_id, banned_id):
    answer = set()
    n = len(banned_id) # 불량 아이디 개수
    perm = list(permutations(user_id, n)) # 불량 아이디 개수만큼 user_id의 n개 원소로 순열 생성

    for p in perm:
        cnt = 0
        for i in range(n): # 아이디가 일치하는지 확인
            if not re.match(banned_id[i].replace('*', '.'), p[i]) or len(banned_id[i]) != len(p[i]):
                # 정규 표현식에 맞지 않는 경우, 문자열의 길이가 다른 경우는 순열 i번째 원소랑 banned_id의 i번째 원소가 맞지 않음
                # 정규 표현식 메타문자 . : 줄바꿈 문자 제외하고 모든 문자와 매치된다
                break
            else:
                cnt += 1

        if cnt == n:
            # 순열의 n개 원소로 불량 아디이 목록의 n개 아이디를 만들 수 있으면 answer에 해당 순열을 집합으로 바꿔서 추가
            answer.add(frozenset(p))

    return len(answer) # 개수를 반환

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"] # 응모자 아이디 목록
# banned_id = ["fr*d*", "abc1**"] # 불량 아이디 목록
# answer = solution(user_id, banned_id)
# print(answer)