n = int(input())
answer = 0
place = list(map(int, input().split()))
honey_sum = []
honey_sum.append(place[0])

for i in range(1, n): # 벌꿀합 누적합으로 저장
    honey_sum.append(honey_sum[i - 1] + place[i])

for i in range(1, n-1): # 꿀통이 왼쪽 끝에 있을 경우
    answer = max(answer, honey_sum[n - 2] + honey_sum[i - 1] - place[i])
    # honey_sum[n-2] : 오른쪽 끝에 고정된 벌이 모아오는 꿀
    # honey_sum[i-1] - place[i] : 고정이 아닌 벌이 얼마나 모으는지 for문으로 따져봄
    # 꿀의 합 - 벌의 위치

for i in range(1, n-1): # 꿀통이 오른쪽 끝에 있을 경우
    answer = max(answer,
                 honey_sum[n - 1] - place[0] + honey_sum[n - 1] - honey_sum[i] - place[i])
    # honey_sum[n-1] - place[0] : 왼쪽 끝에 고정인 벌이 모아오는 꿀
    # honey_sum[n-1] - honey_sum[i] - place[i] : 고정이 아닌 벌의 꿀의 합을 누적합으로 계산, 자신의 위치 꿀값을 빼줌

for i in range(1, n-1): # 꿀통이 가운데에 있을 경우
    answer = max(answer, honey_sum[n - 2] - place[0] + place[i])
    # 벌 위치는 양 끝, 꿀 위치는 고정이 아님 -> 꿀 위치를 for문으로 따져봐야 함
    # honey_sum[n-2] - place[0] : 벌들의 위치를 제외한 꿀의 합
    # place[i] : 꿀 위치의 값을 한번 더 더해준다

print(answer)