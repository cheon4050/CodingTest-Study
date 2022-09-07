n=int(input())

d=list(map(int, input().split())) # 초기값으로 N개 저장

for i in range(n-1):
    temp = sorted(list(map(int, input().split())) + d, reverse=True)
    print(temp)
    d = temp[:n] # 큰 순서대로 N개만 저장
    print("큰 순서대로", d)
print(d[n-1])