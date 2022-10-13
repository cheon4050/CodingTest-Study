import sys
input = sys.stdin.readline

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수

if k >= n: # 각 센서마다 집중국을 세우면 되는 경우로 예외 처리
    print(0)
else:
    index = list(map(int, input().split()))
    index.sort()

    diff = [] # 각 구간의 거리를 담은 배열
    for i in range(len(index) - 1):
        diff.append(index[i+1] - index[i]) # 각 구간의 거리를 구해서 배열에 넣는다

    diff.sort() # 거리를 기준으로 오름차순 정렬

    for i in range(k - 1):
        # 해당 구간 끊었을 때 끊겨진 각 구간의 합을 구하는 방법 :
        # 가장 거리가 먼 구간부터 끊어주면 된다
        # 그냥 거리 저장한 배열에서 그 구간 자를 때 마다 전체 합에서 빼주면 된다
        diff.pop() # 거리가 긴 구간부터 잘라주면 된다 = 없앰

    print(sum(diff))