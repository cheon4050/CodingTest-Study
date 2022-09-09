def solution(s):
    numarr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0,len(numarr)):
        # 영어로된 단어를 찾아 숫자로 변환
        s = s.replace(numarr[i],str(i));
    # 숫자 문자열을 자료형 변환
    return int(s)