def solution(n, k, cmd):
    #링크드리스트 선언
    linked_list = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    k += 1
    #결과값 배열
    result = ["O"] * (n)
    stack = []
    for s in cmd:
        count = 0
        if len(s) > 1:
            _, count = s.split()
            count = int(count)
        # 연결되어 있는 링크드리스트를 적힌 숫자 만큼 이동
        if s[0] == "D":
            for _ in range(count):
                k = linked_list[k][1]
        elif s[0] == "U":
            for _ in range(count):
                k = linked_list[k][0]
        # 지우기
        elif s[0] == "C":
            prev, next = linked_list[k]
            #현재위치와 연결되어 있던 prev, next 저장
            stack.append((k, prev, next))
            #없어진 자료 체크
            result[k - 1] = "X"

            # 첫번째일 경우
            if prev == 0:
                k = linked_list[k][1]
                linked_list[next][0] = prev
            # 마지막일 경우
            elif next == n + 1:
                k = linked_list[k][0]
                linked_list[prev][1] = next
            # 이외에는 삭제한 양옆의 리스트를 연결
            else:
                k = linked_list[k][1]
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        # 복구
        elif s[0] == "Z":
            # 저장했던 자료 pop
            a, prev, next = stack.pop()
            # 다시 저장된 자료 체크
            result[a - 1] = "O"
            #첫번째 일 경우
            if prev == 0:
                linked_list[next][0] = a
            #마지막 일 경우
            elif next == n + 1:
                linked_list[prev][1] = a
            # 그 이외의 경우
            else:
                linked_list[prev][1] = a
                linked_list[next][0] = a
    return "".join(result)

# 정확성 통과
# def solution(n, k, cmd):
#     arr = [i for i in range(n)]
#     stack = []
#     for s in cmd:
#         method = ""
#         count = 0
#         if len(s) > 1:
#             method, count = s.split()
#             count = int(count)
#         if s[0] == "D":
#             k = k+count
#         if s[0] == "U":
#             k = k-count
#         if s[0] == "C":
#             stack.append((k, arr[k]))
#             if k+1 == len(arr):
#                 arr.pop()
#                 k -= 1
#             else:
#                 arr = arr[:k] + arr[k+1:]
#         if s[0] == "Z":
#             a, b = stack.pop()
#             if a<=k:
#                 k+=1
#             arr = arr[:a] + [b]+ arr[a:]
#     cnt = 0
#     result = ""
#     for i in range(n):
#         if cnt >= len(arr):
#             result += "X"
#         elif arr[cnt] == i:
#             result += "O"
#             cnt+=1
#         else:
#             result += "X"
#     return result