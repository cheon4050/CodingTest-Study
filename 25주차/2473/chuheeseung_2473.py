# python3 시간 초과 / pypy 해결
import sys
input = sys.stdin.readline

n = int(input())
liquid = [int(x) for x in input().split()]
liquid.sort() # 투포인터 사용하려고 정렬
tmp = float('inf')
sol = []

for i in range(n - 2):
    # 투포인터 처음과 끝에서 시작 -> 중간에서 만나면 탐색 종료
    # 고정된 용액의 인덱스를 i로 놓음 -> i+1 ~ n-1 구간에서 고정된 용액과의 합이 0과 가까운 두 용액을 찾는다
    fix = liquid[i]
    s = i + 1
    e = n - 1

    while s != e:
        if abs(liquid[s] + liquid[e] + fix) < tmp: # 세 용액의 합의 절대값이 tmp보다 작은 경우
            tmp = abs(liquid[s] + liquid[e] + fix)
            sol = [fix, liquid[s], liquid[e]] # sol 배열에서 정답으로 갱신

        if liquid[s] + liquid[e] + fix == 0: # 0이면 while문 종료
            break
        elif liquid[s] + liquid[e] + fix < 0: # 0보다 작으면 처음 포인터 이동
            s += 1
        else: # 0보다 크면 끝 포인터 이동
            e -= 1

print(*sol)