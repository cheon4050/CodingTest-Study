import sys

input = sys.stdin.readline
T = int(input())


def multiply(arr):
    num = 1
    for n in arr:
        num *= n
    return num


for _ in range(T):
    n = int(input())
    clothes_dict = {}
    for i in range(n):
        clothes, typ = input().split()
        if not typ in clothes_dict:
            clothes_dict[typ] = 1
        clothes_dict[typ] += 1
    clothes_arr = list(clothes_dict.values())
    result = multiply(clothes_arr)-1
    print(result)
