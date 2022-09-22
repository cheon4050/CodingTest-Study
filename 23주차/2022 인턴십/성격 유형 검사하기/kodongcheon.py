def solution(survey, choices):
    mbti_dict = {}
    survey_arr = []
    answer = ''

    for i in ["RT", "CF", "JM", "AN"]:
        mbti_dict[i] = 0

    for i in range(len(survey)):
        if survey[i] in ["TR", "FC", "MJ", "NA"]:
            survey[i] = survey[i][1] + survey[i][0]
            choices[i] = 8 - choices[i]
        choices[i] -= 4

    for i in range(len(survey)):
        mbti_dict[survey[i]] += choices[i]

    for i in mbti_dict:
        if mbti_dict[i] > 0:
            answer += i[1]
        else:
            answer += i[0]
    return answer