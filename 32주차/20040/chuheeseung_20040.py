import sys
input = sys.stdin.readline

answer = 0 # 차례 횟수 세는 변수
n, m = map(int, input().split()) # n : 점의 개수, m : 차례 개수
lines = [i for i in range(n)] # i번째 차례에 해당 플레이어가 선택한 두 점의 번호

def find(x):
    if x == lines[x]:
        return x

    lines[x] = find(lines[x])
    return lines[x]

def union(x, y):
    global i, answer
    x = find(x)
    y = find(y)

    if x == y: # x와 y의 부모가 같으면 게임 끝
        answer = i + 1
    else: # x와 y의 부모가 다르면 합쳐줌
        if x < y:
            lines[y] = x
        else:
            lines[x] = y

for i in range(m):
    x, y = map(int, input().split())

    if not answer:
        union(x, y) # union()으로 입력받은 두개의 점을 합친다

print(answer) # 최종 횟수를 출력