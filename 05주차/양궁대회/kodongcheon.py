def solution(n, info):
    arr = []
    result = []
    result2 = []
    max_value = 0

    # appeach의 화살보다 1개더 많이 쏜 화살 배열 만들기
    for num in info:
        arr.append(num + 1)

    a(arr, 0, "", result, n)

    # lion이 이기는 배열을 찾고, 차이가 가장 큰 배열들 찾는 부분
    for re in result:
        count = check(re, info)
        if count != 0:
            if max_value < count:
                max_value = count
                result2 = [re]
            elif max_value == count:
                result2.append(re)
    # 이길 수 없는 경우 [-1] 리턴
    if not result2:
        return [-1]

    # 화살이 남으면 0점에 나머지 추가
    for i in range(len(result2)):
        if sum(result2[i]) != n:
            result2[i][-1] = result2[i][-1] + n - sum(result2[i])

    # 가장 낮은점수를 더 많이 맞힌 순으로 정렬
    result2.sort(
        key=lambda x: (-x[-1], -x[-2], -x[-3], -x[-4], -x[-5], -x[-6], -x[-7], -x[-8], -x[-9], -x[-10], -x[-11]))

    # 가장 낮은점수 많이 맞힌 첫번 째 배열 리턴
    return result2[0]


# 전체 경우의수 찾기
def a(arr, cnt, str_in, result, n):
    if cnt > 10:
        temp_arr = [int(i) for i in str_in]
        if sum(temp_arr) <= n:
            result.append(temp_arr)
        return
    a(arr, cnt + 1, str_in + str(arr[cnt]), result, n)
    a(arr, cnt + 1, str_in + "0", result, n)


# lion과 apeach 차이 check
def check(arr, info):
    lion = 0
    apeach = 0
    for i in range(11):
        if arr[i] == 0 and info[i] == 0:
            continue
        elif arr[i] > info[i]:
            lion += 10 - i
        else:
            apeach += 10 - i
    if lion > apeach:
        return lion - apeach
    return 0