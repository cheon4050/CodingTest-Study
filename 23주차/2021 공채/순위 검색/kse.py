
# def set_default(obj,idx,val):
#     return obj[idx] or val
#
# #lower bound
# def lower_bound_helper(list, begin, end, is_pivot):
#     mid = (begin + end) >> 1 # a * 2(-1승)
#     if begin == end:
#         return begin
#     if is_pivot(list[mid]):
#         return lower_bound_helper(list, begin, mid, is_pivot)
#     else:
#         return lower_bound_helper(list, mid+1, end, is_pivot)
#
# def lower_bound(list, is_pivot):
#     return lower_bound_helper(list,0,list.length,is_pivot)
#
# def find_greater_or_eq(list, pivot):
#     pivot = +pivot


def solution(info, query):
    answer = []
    language = {}
    job = {}
    career = {}
    food = {}
    scores = {}
    for i in range(len(info)):
        temp = info[i].split(' ')
        if temp[0] not in language.keys():
            language[temp[0]] = [i]
        else:
            language[temp[0]].append(i)
        if temp[1] not in job.keys():
            job[temp[1]] = [i]
        else:
            job[temp[1]].append(i)
        if temp[2] not in career.keys():
            career[temp[2]] = [i]
        else:
            career[temp[2]].append(i)
        if temp[3] not in food.keys():
            food[temp[3]] = [i]
        else:
            food[temp[3]].append(i)
        scores[i] = int(temp[4])

    for q in query:
        temp = q.split(' ')
        candidate = set([i for i in range(len(info)) if scores[i] >= int(temp[7])])
        for t in range(len(temp)):
            if (not temp[t] == '-') and (not temp[t] == 'and'):
                if t == 0:
                    candidate = candidate & set(language[temp[t]])
                elif t == 2:
                    candidate = candidate & set(job[temp[t]])
                elif t == 4:
                    candidate = candidate & set(career[temp[t]])
                elif t == 6:
                    candidate = candidate & set(food[temp[t]])
        answer.append(len(candidate))
    return answer

# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))