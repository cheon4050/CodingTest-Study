import sys
arr = [list(map(int, input())) for _ in range(9)]
def fun(cnt, arr):
    if cnt == 81:
        for nums in arr:
            for num in nums:
                print(num, end="")
            print()
        sys.exit()
    i = cnt // 9
    j = cnt % 9
    if arr[i][j] !=0:
        fun(cnt+1,arr)
        return
    temp = set(arr[i])
    for t in range(9):
        temp.add(arr[t][j])
    for a in range(i//3*3, i//3*3+3):
        for b in range(j//3*3, j//3*3+3):
            temp.add(arr[a][b])
    temp = set([1,2,3,4,5,6,7,8,9]) - temp
    for t in temp:
        arr[i][j] = t
        fun(cnt+1, arr)
    arr[i][j]=0

fun(0, arr)
