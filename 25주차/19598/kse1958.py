import heapq as h

N = int(input())
room = []
for i in range(N):
    room.append(list(map(int, input().strip().split())))
room.sort()  # 시작 시간 -> 끝나는 시간 기준으로 정렬

answer = 0
heap = [room[0][1]]  # 끝나는 시간
h.heapify(heap) #heap으로 변환(O(n))
for arr in room[1:]: #1부터 시작
    # print(arr)
    # 힙에 넣을지 판단은 arr의 시작 시간과 힙에 있는 끝나는 시간을 비교함으로써
    # print("heap: ", heap)
    if heap[0] > arr[0]: #시작 시간과
        h.heappush(heap, arr[1])
    else:
        h.heapreplace(heap, arr[1])
    answer = max(answer, len(heap)) # 회의실 개수
print(answer)