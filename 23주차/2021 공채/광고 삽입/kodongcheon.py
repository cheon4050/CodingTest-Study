def solution(play_time, adv_time, logs):
    MAX_TIME = 100 * 3600 + 1
    prefixSum = [0] * (MAX_TIME)
    advHour, advMin, advSec = map(int, adv_time.split(":"))
    adv_time = advHour * 3600 + advMin * 60 + advSec
    for i in range(len(logs)):
        start, end = logs[i].split("-")
        startHour, startMin, startSec = map(int, start.split(":"))
        endHour, endMin, endSec = map(int, end.split(":"))
        prefixSum[startHour * 3600 + startMin * 60 + startSec] += 1
        prefixSum[endHour * 3600 + endMin * 60 + endSec] -= 1
    for i in range(1, MAX_TIME):
        prefixSum[i] += prefixSum[i - 1]
    result = 0
    check = sum(prefixSum[:adv_time])
    maxCheck = check

    for i in range(adv_time, MAX_TIME):
        check += prefixSum[i] - prefixSum[i - adv_time]
        if check > maxCheck:
            maxCheck = check
            result = i - adv_time + 1

    Hour = str(result // 3600)
    Hour = "0" * (2 - len(Hour)) + Hour
    result -= result // 3600 * 3600
    Minute = str(result // 60)
    Minute = "0" * (2 - len(Minute)) + Minute
    result -= result // 60 * 60
    Seconds = str(result % 60)
    Seconds = "0" * (2 - len(Seconds)) + Seconds

    return Hour + ":" + Minute + ":" + Seconds