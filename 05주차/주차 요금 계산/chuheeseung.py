import math

def minuteChange(time): # 시간을 분으로 변환하는 함수
    hour, min = map(int, time.split(":"))
    return hour * 60 + min

def solution(fees, records):
    answer = []
    dt, df, ut, uf = fees # 기본시간, 기본요금, 단위시간, 단위요금

    dic = dict()

    for r in records:
        time, number, inout = r.split()
        number = int(number)

        if number in dic: # 딕셔너리 생성
            dic[number].append([minuteChange(time), inout])
        else:
            dic[number] = [[minuteChange(time), inout]]

    recordsList = list(dic.items()) # (k, v) 튜플 형태의 리스트로 변환
    recordsList.sort(key=lambda x : x[0]) # 차량 번호를 기준으로 정렬
    print(recordsList)

    for r in recordsList: # 시간 계산하는 부분에서 막혔음
        t = 0

        for rr in r[1]:
            if rr[1] == "IN": # in이면
                t -= rr[0] # 시간을 빼기
            else: #out이면
                t += rr[0] # 시간을 더하기

        if r[1][-1][1] == "IN": # 마지막 출차 내역이 없는 경우
            t += minuteChange('23:59') # 출차 시간을 23:59로 간주

        if t <= dt: # 기본시간보다 작으면 기본요금을 추가
            answer.append(df)
        else: # 기본시간 이상이면 시간 계산
            answer.append(df + math.ceil((t - dt) / ut) * uf)
    return answer


print(solution([180, 5000, 10, 600],
      ["05:34 5961 IN",
       "06:00 0000 IN",
       "06:34 0000 OUT",
       "07:59 5961 OUT",
       "07:59 0148 IN",
       "18:59 0000 IN",
       "19:09 0148 OUT",
       "22:59 5961 IN",
       "23:00 5961 OUT"]))