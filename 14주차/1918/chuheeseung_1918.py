# 1. 피연산자가 들어오면 바로 출력
# 2. 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것을 빼고 자신을 스택에 담음
# 3. 여는 괄호를 만나면 무조건 스택에 담음
# 4. 닫는 괄호를 만나면 여는 괄호를 만날 때까지 스택에서 출력
# 연산자 우선순위 : () > */ > +-

expression = input() # 입력받은 중위표기식
stack = []
answer = "" # 출력할 후위표기식

for s in expression:
    if s == '+' or s == '-': # +- 보다 우선순위가 낮은 연산자 없음 -> 자신보다 우선순위가 높은 것들을 모두 answer에 추가
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop() # 같은 우선순위에 있는 연산자는 모두 결과문자열에 추가
        stack.append(s) # 현재 문자를 다시 스택에 추가
    elif s == '(': # 여는 괄호 : 무조건 스택에 담는다
        stack.append(s)
    elif s == ')': # 닫는 괄호 : 여는 괄호가 가장 뒤에 있을 때까지 pop 한후 출력
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    else: # 피연산자 : 스택에 넣지 않고 바로 출력
        answer += s

while stack: # 남아있는 stack을 pop -> answer에 추가
        answer += stack.pop()

print(answer)