def solution(n, k):
    answer = 0
    _n = ""

    while n: # n을 k진법으로 변환한 문자열로 바꿔줌
        _n = str(n % k) + _n
        n = n // k

    _nList = _n.split('0') # 0을 기준으로 n 분류해서 배열에 넣음

    for i in _nList: # 문자열을 숫자로 변환해서 소수인지 판단하는 for문
        if len(i) == 0: # 소수가 아닌 0, 1, 빈 공간이면 continue로 건너뜀
            continue
        if int(i) < 2:
            continue

        decimal = True # 소수인지 판별하는 true, false 값
        for j in range(2, int(int(i)**0.5) + 1):
            # range 범위 제곱근값으로 작은 부분에서 처리를 해줘야 시간 초과가 안남 -> 막혔던 부분!
            if int(i) % j == 0:
                decimal = False
                break

        if decimal: # 소수라고 판단하면 answer += 1
            answer += 1

    return answer



print(solution(437674, 3))