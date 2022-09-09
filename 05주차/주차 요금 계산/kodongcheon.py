import math
def solution(fees, records):
    #현재 차가 입차되어 있는 목록
    arr1 = {}
    #차가 한번 이상 출차 했던 목록
    arr2 = {}

    results = []
    for record in records:
        clock, car_number, status = record.split()
        #입차 할 경우
        if status == "IN":
            arr1[car_number] = clock
        #출차 할 경우
        else:
            # 한번이라도 출차를 했었으면, 출차했던 것과 합쳐서 계산
            if car_number in arr2:
                arr2[car_number] = arr2[car_number] + (int(clock[:2]) - int(arr1[car_number][:2]))* 60 + int(clock[-2:]) - int(arr1[car_number][-2:])
            # 출차한적이 없다면 현재 출차한거 까지만 계산
            else:
                arr2[car_number] = (int(clock[:2]) - int(arr1[car_number][:2]))* 60 + int(clock[-2:]) - int(arr1[car_number][-2:])
            # 출차햇으니 arr1에서 제거
            del arr1[car_number]
    # 출차를 안한 차가 있으면 계산
    for car_number in arr1:
        if car_number in arr2:
            arr2[car_number] = arr2[car_number] + (23 - int(arr1[car_number][:2]))* 60 + 59 - int(arr1[car_number][-2:])
        else:
            arr2[car_number] = (23 - int(arr1[car_number][:2]))* 60 + 59 - int(arr1[car_number][-2:])
    # 차 넘버 오름차순으로 정렬
    arr2 = sorted(arr2.items())
    # 계산한 가격 배열에 입력
    for car_number, time in arr2:
        if time <= fees[0]:
            result = fees[1]
        else:
            result = fees[1] + math.ceil((time-fees[0])/fees[2]) * fees[3]
        results.append(result)
    return results