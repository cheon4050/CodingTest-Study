n = int(input())
result = 0

for i in range(1, n + 1):
    m = list(map(int, str(i))) # 숫자 자리별로 하나씩 배열 m에 넣어줌
    s = i + sum(m) # 분해합
    
    if(s == n): # 분해합 결과와 n이 같으면
        result = i
        break
        
print(result)