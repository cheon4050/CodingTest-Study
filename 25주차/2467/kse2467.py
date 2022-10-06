n=int(input())
arr=list(map(int,input().split()))
# print(arr)
# n=5
# arr=[-99,-2,-1,4,98]
# n=4
# arr=[-100, -2, -1,103]

#a[-1]-a[0] -> a[-2]-a[1]
def binary_search(target, N):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True, mid # 함수를 끝내버린다.
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False, start

result = []
if arr[-1] <= 0: # 모두 아칼리
    result = [arr[-2], arr[-1]]
elif arr[0] >= 0: # 모두 산성
    result = [arr[0], arr[1]]
else:
    right = binary_search(0, n)[1]
    left = right - 1
    result = [arr[left], arr[right]]
    minValue = abs(arr[left] + arr[right])

    if left > 0 and abs(arr[left-1] + arr[left]) < minValue: # 아칼리 / 아칼리가 최소일때
        minValue = abs(arr[left-1] + arr[left])
        result = [arr[left-1], arr[left]]

    if right < n - 1 and abs(arr[right] + arr[right+1]) < minValue: # 산성 / 산성이 최소일때
        minValue = abs(arr[right] + arr[right+1])
        result = [arr[right], arr[right+1]]

    if arr[right] == 0 and arr[right+1] < minValue:
        result = [arr[right], arr[right+1]]
        minValue = arr[right+1]
        right += 1

    while left>=0 and right<n and minValue > 0:
        value = arr[left] + arr[right]
        absValue = abs(value)
        if absValue < minValue:
            minValue = absValue
            result = [arr[left], arr[right]]

        # move
        if value > 0: # left move
            left -= 1
        else: # right move
            right += 1

print(' '.join( map(str, result)))


'''
answer=[]
match=dict()
temp=float('inf')
def check_app(temp):
    return sorted(temp, key=lambda x: (abs(x), -x))[0]

for num in range(n//2):
    temp=arr[-(num+1)]+arr[num]
    answer.append(temp)
    match[temp]=[arr[-(num+1)], arr[num]]

result=match[check_app(answer)]

print(*sorted(result))
'''