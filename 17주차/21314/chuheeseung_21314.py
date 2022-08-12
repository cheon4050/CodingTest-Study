num = input() # 민겸수
min, max = '', ''
m = 0 # k가 나오기 전의 m 개수

for n in num:
    if n == "M": # m일 경우 개수 증가
        m += 1
    else: # k일 경우 m의 값에 따른 최소, 최대를 구함
        if m > 0:
            min += str(10 ** m + 5)
            max += str(5 * (10 ** m))
        else: # m ==0 인 경우
            min += '5'
            max += '5'
        m = 0 # m 초기화

if m > 0: # 마지막이 m으로로끝났을 경우
    min += str(10 ** (m - 1))
    max += '1' * m

print(max) # 최댓값 최솟값 출력
print(min)

# 최솟값
    # k로 끝날 때 마다 10 ** (k가 나오기 전 m 개수) + 5 추가
    # m으로 끝날 때 마다 10 ** (m 개수 - 1) 추가
# 최댓값
    # k로 끝날 때 마다 5 * (10 ** (k 나오기 전 m 개수)) 추가
    # m으로 끝날 때 마다 (m 개수) + 1 추가