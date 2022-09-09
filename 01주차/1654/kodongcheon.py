k, n = map(int, input().split())

numberlist = []
for _ in range(k):
    numberlist.append(int(input()))

def solution(num_list, target, left, right):
    cnt = 0
    mid = (left+right)//2
    if left >= right:
        return left - 1
    for i in num_list:
        cnt += i // mid
    if cnt >= target:
        return solution(num_list, target, mid+1, right)
    elif cnt < target:
        return solution(num_list, target, left, mid)
print(solution(numberlist, n, 0, 2**32))


