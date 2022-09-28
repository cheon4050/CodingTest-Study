import math

t = int(input())

for _ in range(t): # t개만큼 for문 반복
    string = input() # 문자열

    if string == string[::-1]: # 회문인지 확인
        print("0")
    else:
        data_start = list(string) # 처음 데이터에서 하나를 뺄 데이터
        data_end = list(string) # 마지막 데이터에서 하나를 뺄 데이터

        for i in range(math.ceil(int(len(string) / 2))): # 홀수인 경우 올림으로 받아온다
            if string[i] != string[-(i + 1)]: # 하나씩 비교하면서 다르면 앞 데이터를 뺄지 뒤 데이터를 뺄지 비교
                data_start.pop(i)
                data_end.pop(-(i + 1))

                if data_start == data_start[::-1]: # 앞 데이터 뺀 경우가 유사회문인 경우
                    print("1")
                    break

                if data_end == data_end[::-1]: # 뒤 데이터 뺀 경우가 유사회문인 경우
                    print("1")
                    break

                print("2") # 일반 문자열인 경우
                break