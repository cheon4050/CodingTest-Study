# 스택
"""
중위 표기 수식을 후위 표기 수식으로 변환하는 알고리즘
infix_to_posfix(exp):

스택 s를 생성하고 초기화
while (exp에 처리할 문자가 남아 있으면)
    ch <- 다음에 처리할 문자
    switch(ch)
    case 연산자:
        while ( peek(s)의 우선순위 >= ch의 우선순위 ) do
            e <- pop(s)
            e를 출력
        push(s, ch);
        break;
    case 왼쪽 괄호 :
        push(s, ch);
        break;
    case 오른쪽 괄호 :
        e <- pop(s);
        while( e != 왼쪽 괄호 ) do
            e를 출력
            e <- pop(s)
        break;
    case 피연산자:
        ch를 풀력
        break;
while ( not is_empty(s) ) do
    e <- pop(s)
    e를 출력

"""
from pythonds.basic.stack import Stack

# class Empty(Exception):
#     pass
# class ArrayStack:
#     def __init__(self):
#         """빈 스택 하나를 생성합니다"""
#         self._data = []
#     def __len__(self):
#         """스택에 저장된 요소의 개수를 반환합니다"""
#         return len(self._data)
#
#     def push(self, e):
#         """스택에 요소를 추가합니다"""
#         self._data.append(e)
#
#     def is_empty(self):
#         """스택이 비어있으면 True를 반환합니다."""
#         return len(self._data) == 0
#     def pop(self):
#         """가장 마지막에 들어온 요소를 반환하고 제거합니다"""
#         if self.is_empty():
#             raise Empty("Stack is empty")
#         return self._data.pop()
#
#     def top(self):
#         """가장 마지막에 들어온 요소를 제거하지 않고 반환합니다"""
#         if self.is_empty():
#             raise Empty("Stack is empty")
#         return self._data[-1]

str = input()

def prec(op): #연산자의 우선순위를 반환한다.
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1


def infix_to_postfix(exp):
    s = []
    result = []
    for i in range(len(exp)):
        ch = exp[i]
        if ch == '+' or ch == '-' or ch == '*' or ch == '/': #연산자
            # 스택에 있는 연산자의 우선순위가 더 크거나 같으면 출력
            while (not len(s) == 0) and (prec(ch) <= prec(s[-1])):
                result.append(s.pop())
            s.append(ch)
        elif ch == '(': #왼쪽 괄호
            s.append(ch)
        elif ch == ')': # 오른쪽 괄호
            top_op = s.pop()
            # 왼쪽 괄호를 만날때까지 출력
            while not top_op == '(':
                result.append(top_op)
                top_op = s.pop()
        else: #피연산자
            result.append(ch)
    while not len(s) == 0:  # 스택에 저장된 연산자들 출력
        result.append(s.pop())
    print("".join(result))


infix_to_postfix(str)
