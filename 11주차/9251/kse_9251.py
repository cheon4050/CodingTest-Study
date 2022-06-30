def LCS(seq1, seq2):
    dp = [[0 for _ in range(1001)] for _ in range(1001)]

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[len(seq1)][len(seq2)]

seq1 = list(input().strip())
seq2 = list(input().strip())

print(LCS(seq1, seq2))