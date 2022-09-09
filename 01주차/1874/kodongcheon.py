import sys
n = int(sys.stdin.readline())

print_list = []
num_list = []
cnt = 1
for i in range(n):
    num = int(sys.stdin.readline())
    if cnt <= num:
        while(cnt<=num):
            print_list.append("+")
            num_list.append(cnt)
            cnt += 1
        print_list.append("-")
        num_list.pop()
    elif cnt > num:
        pop_num = num_list.pop()
        if pop_num != num:
            print("NO")
            break
        else:
            print_list.append("-")
else:
    for number in print_list:
        print(number)

