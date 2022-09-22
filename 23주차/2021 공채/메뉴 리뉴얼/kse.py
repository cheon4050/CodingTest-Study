from itertools import combinations

def solution(orders, course):
    combination_map = {}
    # course 요리 마다 dict 객체 부여
    for c in course:
        combination_map[c] = {}

    for order in orders:
        # 한 손님이 주문한 메뉴목록(문자열)을 배열로 변경후 정렬 (후에 combination 할 때 중복을 없애기 위함)
        # ex) 'WX', 'XW' 는 같은 메뉴목록으로 여겨야 하기 때문
        menus = list(order)
        menus.sort()
        for c in course:
            # 해당 메뉴 목록에서 나올 수 있는 combination 구하기 (단, 코스요리에 맞는 조합이어야 함)
            current_combination = list((map(''.join, combinations(menus, c))))
            for combi in current_combination:
                # 해당 코스요리에 맞는 조합을 hashmap에 삽입
                # 이미 hashmap에 존재한다면 +1 없다면 1로 초기화
                if combi in combination_map[c]:
                    combination_map[c][combi] += 1
                else:
                    combination_map[c][combi] = 1

    # print(combination_map)
    answer = []

    for c in course:
        # 해당 코스 요리중 최대값(제일 많은 사람이 먹은 조합)을 갖는 음식 조합 찾아내기(단 최대값은 1이상 이어야함 - 문제 조건에 2사람 이상이 먹은 조합만을 고려하라고 되어있음)
        eles = [k for k,v in combination_map[c].items() if max(combination_map[c].values()) > 1 and max(combination_map[c].values()) == v]
        for a in eles:
            answer.append(a)

    # 나온 조합들을 sort하여 return
    answer.sort()
    return answer