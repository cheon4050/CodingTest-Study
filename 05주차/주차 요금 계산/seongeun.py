def solution(fees, records):
    a,b,d=[0]*10000,[],{}
    for i in records:
        t,n,io=i.split() #시간, 차량번호, 내역 나눠 넣기
        n=int(n) #차량번호 int화
        h,m = map(int, t.split(':')) #시간 분 초 나눠 넣기
        if io == 'IN': #입차
            d[n]=h*60+m # 누적 주차시간은 분단위로 쌓이니까
        elif io == 'OUT': #출차
            p=d.pop(n) #출차한 차들의 누적 주차시간은 다 p에
            a[n] += h*60+m-p #총 누적 주차시간
    for n,p in d.items(): #d에 남아있는 차들은 다 23:59까지 출차가 되지 않은 차들임
        a[n] += 23*60+59-p 
    for i in a:
        if i !=0:  # 남은 주차시간이 0이 아니면
            if i <= fees[0]: #기본 시간보다 작을 경우에
                b.append(fees[1]) # 기본 요금을 b에 추가
            else:
                b.append(((i - fees[0]-1)//fees[2]+1)*fees[3]+fees[1]) #요금 계산
    return b

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))