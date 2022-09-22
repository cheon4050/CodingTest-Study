def solution(play_time, adv_time, logs):
    # 1. 모든 시간을 '초' 단위로 환산
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    all_time = [0 for i in range(play_time + 1)]
    # play_time의 크기 만큼 모든 시간별 시청자 수를 저장할 배열
    #1초당 시청자 수를 누적해서 기록 (나중에 뺄 때 편하려고)

    # 2. logs 내의 모든 시간을 초로 환산 & start, end 구분
    for l in logs:
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1 # all_time 배열에서 start 시각에 시청중인 사람 수 + 1
        all_time[end] -= 1 # 한명이 시청을 종료했으니까 end 시각에 - 1
        # 누적 기록 과정에서 모든 부분 표시를 해줄 거니까 시작과 끝에만 표시

    # 3. 구간 별 시청자 수 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        # (i-1초 ~ i초) 1초 동안의 시청자 수 기록해서 모든 값 저장

    # 4. 모든 구간 시청자 수 누적 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        # 동일한 코드 한번 더 사용해서 모든 시청자 수를 누적해서 쌓아준다

    # 5. 누적된 시청자 수를 바탕으로 가장 시청자 수가 많은 구간 탐색
    most_view = 0
    max_time = 0

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                # 해당 구간의 시청자 수 = 현재 i초 누적 시청자 수 - (i-adv_time)초의 누적 시청자 수
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    answer = int_to_str(max_time)

    return answer

def str_to_int(time): # 시간 문자열을 초단위로 변환하는 함수
    h, m, s = time.split(":")

    return int(h) * 3600 + int(m) * 60 + int(s)
def int_to_str(time): # 초를 시간 문자열로 변환하는 함수
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)

    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)

    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)

    return h + ':' + m + ':' + s


solution("02:03:55",
         "00:14:15",
         ["01:20:15-01:45:14",
          "00:40:31-01:00:00",
          "00:25:50-00:48:29",
          "01:30:59-01:53:29",
          "01:37:44-02:02:30"])