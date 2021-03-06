t = int(input()) # 테스트 케이스를 입력받음

d = [0] * 11 # n이 11보다 작으니까 11개의 리스트를 생성

d[1], d[2], d[3] = 1, 2, 4 # 1, 2, 3으로 각 수를 나타내는 방법 개수 저장

for i in range(4, len(d)): # 점화식으로 구한 값을 d[i]에 정답값을 넣음
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(t): # 테스트 케이스 개수 만큼 반복
    n = int(input())
    print(d[n])

# 점화식
# 1을 만드는 방법 : (1) 1가지
# 2를 만드는 방법 : (11, 2) 2가지
# 3을 만드는 방법 : (111, 12, 21, 3) 4가지
# d[4] = (d[3] + 1을 한 것) + (d[2]에 + 2를 한 것) + (d[1]에 + 3을 한 것)