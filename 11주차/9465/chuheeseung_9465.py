import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t): # 테스트 케이스만큼 반복
    n = int(input())
    m1 = list(map(int, input().split())) # 첫번째줄 스티커의 점수
    m2 = list(map(int, input().split())) # 두번째줄 스티커의 점수

    for i in range(1, n): # 각 스티커 인덱스의 최대값을 구한다
        if i == 1: # 인덱스가 1일 때 최댓값 = 이전 대각선의 스티커 점수
            m1[1] += m2[0]
            m2[1] += m1[0]
        else: # 인덱스가 1보다 클 때 최댓값 = max(두칸 전 스티커값, 이전 스티커 값) + 현재 스티커값
            m1[i] = max(m2[i-1], m2[i-2]) + m1[i]
            m2[i] = max(m1[i-1], m1[i-2]) + m2[i]

    print(max(m1[n-1], m2[n-1]))