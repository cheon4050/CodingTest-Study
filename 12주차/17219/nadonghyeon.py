N, M = map(int, input().split())
dic = {}
for _ in range(N):
    address, password = input().split()
    dic[address] = password

for _ in range(M):
    print(dic[input().rstrip()])
