while True:
    numbers = input()
    reverse = ""

    if numbers == "0":
        break

    for i in numbers:
        reverse = i + reverse

    if numbers == reverse:
        print('yes')
    else:
        print('no')