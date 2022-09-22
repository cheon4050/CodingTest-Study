from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course: # course 배열에 대해서 반복
        temp = []
        for order in orders:
            combination = combinations(sorted(order), c) # 조합 생성해서 temp에 추가
            temp += combination

        my_dict = Counter(temp) # counter로 조합 리스트에서 각 문자열 갯수를 세고 딕셔너리 형태로 반환
        # Counter(
        #     {('A', 'C'): 4, ('C', 'D'): 3, ('C', 'E'): 3, ('D', 'E'): 3, ('B', 'C'): 2, ('B', 'F'): 2, ('B', 'G'): 2,
        #      ('C', 'F'): 2, ('C', 'G'): 2, ('F', 'G'): 2, ('A', 'D'): 2, ('A', 'E'): 2, ('A', 'B'): 1, ('A', 'F'): 1,
        #      ('A', 'G'): 1, ('A', 'H'): 1, ('C', 'H'): 1, ('D', 'H'): 1, ('E', 'H'): 1})

        if len(my_dict) > 0:
            max_value = max(list(my_dict.values())) # 딕셔너리에서 가장 큰 수

            if max_value >= 2:
                for key, values in my_dict.items():
                    if values == max_value: # 주문 횟수가 2회 이상이고 최댓값인 경우에 answer에 추가
                        answer.append(''.join(map(str, key)))

    answer = sorted(answer)

    return answer

# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])