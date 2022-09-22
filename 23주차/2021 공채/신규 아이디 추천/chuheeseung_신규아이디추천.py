def solution(new_id):
    answer = ''

    new_id = new_id.lower() # 1

    for i in new_id: # 2
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i

    while '..' in answer: # 3
        answer = answer.replace('..', '.')

    if answer[0] == '.': # 4
        answer = answer[1:] if len(answer) > 1 else '.' # 길이가 1인 경우가 있어서 if문 사용
    if answer[-1] == '.':
        answer = answer[:-1]

    if answer == '': # 5
        answer = 'a'

    if len(answer) > 15: # 6
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) < 3: # 7
        answer += answer[-1]

    return answer

# solution("...!@BaT#*..y.abcdefghijklm")
# solution("z-+.^.")
# solution("=.=")
# solution("123_.def")
# solution("abcdefghijklmn.p")