A = input()
B = input()

LCS = [[0]*(len(B)+1) for i in range(len(A)+1)]
for i in range(len(A)):
    for j in range(len(B)):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        if A[i] == B[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
result = 0
for i in LCS:
    result = max(result,max(i))
print(result)
