import math

def solution(n, stations, w):
    answer = 0
    dist = [] # 전파 전달 안되는 구간 저장 리스트

    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1) - (stations[i-1]+w))
        # dist 배열에 전파 닿지 않는 거리 저장

    dist.append(stations[0] - w - 1) # 맨 앞 기지국에서 첫번째 아파트 사이에 전파 닿지 않는 거리 저장
    dist.append(n - (stations[-1] + w)) # 맨 뒤 기지국에서 마지막 아파트 사이에 전파 닿지 않는 거리 저장

    for i in dist:
        if i <= 0: # 닿지 않는 거리가 0 이하일 경우 패스
            continue
        else: # 닿지 않는 거리에 설치할 숭 있는 최소 개수를 answer에 더해줌
            answer += math.ceil(i / (2 * w + 1))
            # 최소로 설치하는 방법 = 전파가 닿지 않는 거리 / (기지국 위치 + 전파가 닿을 거리 * 2) <- 올림

    return answer


# n = 11 # 아파트 개수
# stations = [4, 11]  # 기지국이 설치된 아파트 번호 배열
# w = 1 # 전파 도달 거리
# answer = solution(n, stations, w)
# print(answer)