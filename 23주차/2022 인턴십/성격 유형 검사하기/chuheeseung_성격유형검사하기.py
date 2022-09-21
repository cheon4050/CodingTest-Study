def solution(survey, choices):
    result = [0, 0, 0, 0]
    answer = ''

    for i in range(len(survey)):
        if survey[i][0] == "R":
            result[0] += -(choices[i] - 4)
        elif survey[i][0] == "T":
            result[0] -= -(choices[i] - 4)
        elif survey[i][0] == "C":
            result[1] += -(choices[i] - 4)
        elif survey[i][0] == "F":
            result[1] -= -(choices[i] - 4)
        elif survey[i][0] == "J":
            result[2] += -(choices[i] - 4)
        elif survey[i][0] == "M":
            result[2] -= -(choices[i] - 4)
        elif survey[i][0] == "A":
            result[3] += -(choices[i] - 4)
        elif survey[i][0] == "N":
            result[3] -= -(choices[i] - 4)

    if result[0] >= 0:
        answer = answer + 'R'
    else:
        answer = answer + 'T'

    if result[1] >= 0:
        answer = answer + 'C'
    else:
        answer = answer + 'F'

    if result[2] >= 0:
        answer = answer + 'J'
    else:
        answer = answer + 'M'

    if result[3] >= 0:
        answer = answer + 'A'
    else:
        answer = answer + 'N'

    return answer