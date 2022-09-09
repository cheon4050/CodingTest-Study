n = int(input()) # O 개수
m = int(input()) # 문자열 s의 길이
s = input() # 문자열
p = "IO" * n + "I"
switch = False
count = 1
output = 0

for i in range(m): # 문자열 s를 돈다
    if not switch and s[i] == 'I': # switch가 False인 상태에서 I가 등장하면
        switch = True # switch를 False로 바꿔준다
    elif switch and s[i] != s[i-1]: # switch가 True인 상태에서 이전 인덱스랑 다른 값이면
        count += 1 # count를 증가한다
    else: #switch가 True인 상태에서 이전 인덱스 원소와 동일한 값이 등장하면
        if count >= len(p):
            output += (count- len(p)) // 2 + 1 # 이전 인덱스 원소까지의 구간에 속한 p의 개수를 output에 더해준다
        count = 1
        if s[i] == 'O': # 현재 원소가 'O'이라면 switch를 False로 바꾼다
            switch = False
            # 현재 원소가 I라면 현재 원소부터 다시 IOIOI... 구간이 시작되므로 switch를 그대로 True로 둔다

if count >= len(p): # 마지막에 switch가 True인 상태에서 구간이 끝까지 있는 바람에 output에 p개수를 더하는 과정이 안될 수 있어서 추가
    output += (count - len(p)) // 2 + 1

print(output)
