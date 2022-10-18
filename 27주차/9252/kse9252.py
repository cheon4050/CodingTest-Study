#LCS 2
lcs_list2=[0] + list(input().rstrip())
lcs_list1=[0] + list(input().rstrip())

dp = [[0 for _ in range(len(lcs_list1))] for __ in range(len(lcs_list2))]

for i in range(1, len(lcs_list2)):
    for j in range(1, len(lcs_list1)):
        if lcs_list2[i] == lcs_list1[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

row = len(lcs_list2) - 1
col = len(lcs_list1) - 1
ans = ""
while dp[row][col]:
    if dp[row][col] == dp[row - 1][col]:
        row -= 1
    elif dp[row][col] == dp[row][col - 1]:
        col -= 1
    else:
        ans = lcs_list2[row] + ans
        row -= 1
        col -= 1

print(dp[len(lcs_list2) - 1][len(lcs_list1) - 1])
print(ans)