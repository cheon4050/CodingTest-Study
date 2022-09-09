N = int(input()) #이동하려고 하는 채널 N
M = int(input()) #둘째 줄에는 고장난 버튼의 개수
disabled_btn = []  # 고장난 버튼 리스트

if M>0:
    disabled_btn = input().split()
result=abs(N-100) # 100부터 시작
need_channels = [] # 조건에 맞는 채널만 담을 리스트

for i in range(0,1000001):
    possible = True
    for j in disabled_btn:
        if j in str(i):
            possible = False
            break
    if possible:
        need_channels.append(i)

for k in need_channels: # 리스트에서 MIN 값 찾기
    if abs(k-N) +len(str(k)) < result:
        result = abs(k-N) +len(str(k))

print(result)


# N = int(input()) #이동하려고 하는 채널 N
# M = int(input()) #둘째 줄에는 고장난 버튼의 개수
# disabled_btn = []  # 고장난 버튼 리스트
#
# def search_c(n, dis_btn):
#     result=abs(n-100) #100부터 시작
#     for i in range(0,1000001):
#         possible=True
#         for j in str(i):
#             if j in dis_btn:
#                 possible=False
#                 break
#         if possible:
#             result=min(result, abs(n-i)+len(str(i)))
#     return result
#
# if(M>0):
#     disabled_btn = input().split()
#     answer = search_c(N, disabled_btn)
#
# print(answer)