n, k = map(int, input().split())
wallet = [] # 동전 담는 지갑 리스트
count = 0 # 동전의 개수를 저장할 변수

for i in range(n): # 동전의 종류만큼 반복
    coin = int(input()) # 동전의 값을 리스트에 추가
    wallet.append(coin)

wallet.reverse() # 리스트를 내림차순으로 정렬
# -> 그리디 알고리즘에서는 최고의 선택을 해야함
# -> 동전의 개수가 가장 적은게 좋은 선택 -> 가장 큰 단위의 동전부터 계산해줘야 한다

for coin in wallet: # 지갑 리스트 돌면서 for문
    count += k // coin # 동전의 개수 = 코인으로 나눈 몫
    k %= coin # 잔돈 = 나머지

print(count) # 동전의 개수를 출력