import re
from itertools import permutations

def check(users,banned_id):
    #각 조합과 banned_id 목록 비교
    for i in range(len(banned_id)):
        #글자 길이 비교
        if len(users[i]) != len(banned_id[i]):
            return False

        #각 글자 비교
        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False # 현재 튜플 불일치
    return True

def solution(user_id, banned_id):

    #banned_id 개수만큼 가능한 모든 user_id의 순열(튜플)로 리스트 생성
    user_permutation = list(permutations(user_id,len(banned_id)))
    bannedList = []

    for users in user_permutation: #하나의 튜플과 비교 시작
        if not check(users, banned_id):
            continue # 다음 튜플 가져오기
        else:
            users = set(users)
            if users not in bannedList:
                bannedList.append(users)

    return len(bannedList)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))