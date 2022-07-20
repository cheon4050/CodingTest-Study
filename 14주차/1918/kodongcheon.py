# s = input().rstrip()
#
# def ss(s):
#     susik = ["+", "-"]
#     stack = ["("]
#     for i in range(len(s)):
#         if s[i] == "(" or s[i] == ")":
#             stack.append(s[i])
#             stack.append(s[i])
#         elif s[i] in susik:
#             stack.append(")")
#             stack.append(s[i])
#             stack.append("(")
#         else:
#             stack.append(s[i])
#     stack.append(")")
#     return "".join(stack)
#
# s = ss(s)
# print(s)
# #괄호
# stack1 = []
# #알파벳
# stack2 = []
# #수식
# stack3 = []
# susik = ["+", "-", "*", "/"]
# result = ""
#
# for i in range(len(s)):
#     if s[i] == "(":
#         stack1.append("(")
#     elif s[i] == ")":
#         stack1.pop()
#         if not stack1:
#             result += "".join(stack2)
#             result += "".join(stack3[::-1])
#             stack2 = []
#             stack3 = []
#     elif s[i] in susik:
#         stack3.append(s[i])
#     else:
#         stack2.append(s[i])
#
# print(result)

expression = input()

stack = []
ans = ""
for s in expression:
    if s == '+' or s == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(s)
    elif s == '(':
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    else:
        ans += s

while stack:
    ans += stack.pop()

print(ans)