brackets = input()
stack = []
number_of_iron_sticks = 0
for index, bracket in enumerate(brackets):
    if bracket == "(":
        stack.append("(")
    else:
        stack.pop()
        if brackets[index-1] == "(":
            number_of_iron_sticks += len(stack)
        else:
            number_of_iron_sticks += 1

print(number_of_iron_sticks)
