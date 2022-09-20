from itertools import combinations

def solution(orders, course):
    result = []
    for c in course:
        arr = {}
        for order in orders:
            order = sorted(order)
            for oo in list(combinations(list(order), c)):
                if oo in arr:
                    arr[oo] += 1
                else:
                    arr[oo] = 1

        result += ["".join(k)
                   for k, v in arr.items() if max(arr.values()) == v and v >= 2]
    return sorted(result)