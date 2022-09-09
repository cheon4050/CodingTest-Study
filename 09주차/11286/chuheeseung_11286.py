import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
        # 힙에 원소를 추가할 때 (-i, i) 튜플 형태로 넣어주면 튜플의 첫번째 원소를 기준으로 힙을 구성하게 된다
        # 실제 값은 튜플의 두번재 자리에 저장되어 있으니까 [1] 인덱싱으로 접근해주면 된다