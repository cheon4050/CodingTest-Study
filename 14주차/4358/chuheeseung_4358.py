import sys
from collections import defaultdict
input = sys.stdin.readline

trees = defaultdict(int)
count = 0 # 전체 나무 수

while True:
    n = str(input().rstrip())

    if not n:
        break

    trees[n] += 1 # 해당 나무 값에 + 1
    count += 1

trees = sorted(trees.items()) # 사전순으로 출력하기 위해 정렬

for k, v in trees:
    print("%s %.4f" % (k, round((v / count * 100), 4))) # 소수 넷째자리까지 출력