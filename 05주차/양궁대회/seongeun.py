score_table = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
max_score = 0

def get_score(apeach, lion):
    score = 0
    for i in range(len(apeach)):
        if apeach[i] > lion[i]:
            score -= score_table[i]
        elif apeach[i] < lion[i]:
            score += score_table[i]
    return score

def helper(n, apeach, lion, answer, visited):
    global max_score
    if n == 0:
        score = get_score(apeach, lion)
        if score <= 0:
            return
        elif score == max_score:
            answer.append([_ for _ in lion])
        elif score > max_score:
            answer.clear()
            answer.append([_ for _ in lion])
            max_score = score
        return

    elif n > 0:
        for i in range(len(lion)):
            if not visited[i]:
                visited[i] = True
                lion[i] = n if i == len(lion)-1 else apeach[i]+1
                helper(n - lion[i], apeach, lion, answer, visited)
                lion[i] = 0
                visited[i] = False

def solution(n, info):
    answer, lion, visited = [], [0 for _ in info], [0 for _ in info]
    helper(n, info, lion, answer, visited)
    return sorted(answer)[0] if answer else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))