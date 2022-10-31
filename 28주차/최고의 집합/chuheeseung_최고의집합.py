def solution(n, s):
    answer = []

    if s // n < 1: # n개의 숫자로 s를 만들 수 없는 경우
        answer = [-1]
    else:
        s_n = s // n #

        for i in range(n):
            answer.append(s_n)

        s_p_n = s % n
        idx = len(answer) - 1

        for i in range(s_p_n):
            answer[idx-i] = answer[idx-i] + 1

    return answer

# n = 2 # 집합의 원소의 개수
# s = 9 # 모든 원소들의 합
# answer = solution(n, s)
# print(answer)