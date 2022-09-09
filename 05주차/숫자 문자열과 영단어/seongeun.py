def solution(s):
    answer = ''
    eng = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0' }

    num = ''
    for word in s:
        if word.isdigit():
            answer += word
        else:
            num += word
            if num in eng.keys():
                answer += eng[num]
                num = ''

    return int(answer)
print(solution("one4seveneight"))