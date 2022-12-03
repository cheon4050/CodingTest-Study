def solution(n, stations, w):
    answer = 0
    station=0
    temp=1

    while(temp<=n):
        if (station < len(stations)) and (temp >=(stations[station]-w)):
            temp=stations[station]+w+1
            station+=1
        else:
            answer+=1
            temp+=(w*2)+1
    return answer

print(solution(11, [4, 11], 1))