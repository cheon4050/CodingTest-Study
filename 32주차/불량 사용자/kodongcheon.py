from itertools import product

def solution(user_id, banned_id):
    idDict = {}
    for banId in banned_id:
        idDict[banId] = []
        for userId in user_id:
            if len(userId) == len(banId):
                for i in range(len(userId)):
                    if banId[i] == "*":
                        continue
                    elif userId[i] != banId[i]:
                        break
                else:
                    idDict[banId].append(userId)

    arr = []
    for banId in banned_id:
        arr.append(idDict[banId])
    arr = list(product(*arr))
    result = []
    for ar in arr:
        if len(set(ar)) == len(ar):
            ar = sorted(ar)
            if not ar in result:
                result.append(ar)

    return len(result)
