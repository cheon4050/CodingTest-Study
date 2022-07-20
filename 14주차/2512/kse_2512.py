# 시간 초과 (Pypy3로는 통과)
# N = int(input())
# city = list(map(int,input().split()))
# budget = int(input())
# max_city = max(city)
# sum_city = sum(city)
#
# if sum_city > budget:
#     while sum_city>budget:
#         for i in range(N):
#             if max_city == city[i]:
#                 city[i] -= 1
#                 sum_city -= 1
#         max_city -= 1
#
# print(max_city)

N = int(input())
city = list(map(int,input().split()))
budget = int(input())

max_city = max(city)
min_city = 1

while max_city >= min_city:
    mid = (max_city + min_city) // 2
    tmp = 0

    for val in city:
        if mid < val :
            tmp += mid
        else :
            tmp += val

    if tmp > budget:
        max_city = mid - 1
    else:
        min_city = mid + 1

print(max_city)