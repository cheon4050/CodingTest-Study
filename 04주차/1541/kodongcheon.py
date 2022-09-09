str_in = input()
str_in = "(" + str_in
i = 2
while(len(str_in) != i):
    if str_in[i] == "-":
        str_in = str_in[:i] + ")" + "-" + "(" + str_in[i + 1:]
        i += 1
    i+=1
str_in = str_in + ")"
stack = []
temp_string = ""
# 0숫자 제거
for i in range(len(str_in)):
    if str_in[i] == "(" or str_in[i] == "+" or str_in[i] == "-" or str_in[i]==")":
        if len(temp_string) != 0:
            stack.append(str(int(temp_string)))
            temp_string = ""
            stack.append(str_in[i])
        else:
            stack.append(str_in[i])
    else:
        temp_string += str_in[i]
print(eval("".join(stack)))
