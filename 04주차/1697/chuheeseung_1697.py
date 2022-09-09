import sys
from collections import deque

input = sys.stdin.readline

MAX_SIZE = 100000 # n, k의 크기 제한사항
n, k = map(int, input().split()) # n, k를 입력 받고 
dist = [0] * (MAX_SIZE + 1) # dist 배열 최대수만큼 생성해서 0으로 초기화

def bfs():
    b = deque() # 큐를 빠르게 해주기 위해서 deque으로 설정
    b.append(n) # 수빈이가 있는 위치(출발점)를 넣어줌

    while b: # b가 정수일 때 계속 반복
        x = b.popleft() # 제일 왼쪽 값을 뽑아서 x에 저장

        if x == k: # 동생이 있는 위치 k랑 같으면 
            print(dist[x]) # 배열 값 출력
            break

        for j in (x-1, x+1, x*2): # 이동하는 경우의수 세가지를 j에 순서대로 넣어줌
            if 0 <= j <= MAX_SIZE and not dist[j]: 
                # 0 <= j <= MAX_SIZE이고 dist[j]가 0 값을 가지면 dist[x] + 1 해준걸 dist[j]에 추가
                dist[j] = dist[x] + 1
                b.append(j) # 값을 찾을때까지 반복

bfs()