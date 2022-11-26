def solution(n, stations, w):
    cnt = 0
    start = stations[0] - w
    end = stations[0] + w
    stations = stations[1:]
    for station in stations:
        if station - w <= end+1:
            end = station+w
            continue
        else:
            null = station - w - (end+1)
            cnt += null // (2*w+1)
            if null%(2*w+1):
                cnt += 1
            end = station+w
    if start > 1:
        cnt += (start-1) // (2*w+1)
        if (start-1)%(2*w+1):
            cnt += 1
    if end < n:
        cnt += (n-end) // (2*w+1)
        if (n-end)%(2*w+1):
            cnt += 1

    return cnt