def solution(n, works):
    answer = 0
    works.sort(reverse = True) # 일을 내림차순으로 정렬

    while n > 0 and works[0] != 0:
        count = works.count(works[0])

        if count == len(works):
            sub = 1
        else:
            sub = works[0] - works[count]

        for i in range(0, count * sub):
            if n - 1 >= 0:
                works[i%count] = works[i%count] - 1
                n = n - 1
            else:
                break

    for x in works:
        answer += x * x

    return answer

# works = [4, 3, 3]
# n = 4
# result = 12
# answer = solution(works, n, result)
# print(answer)