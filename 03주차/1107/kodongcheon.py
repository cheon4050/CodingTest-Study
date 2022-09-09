N = input()
M = int(input())
arr = []
result = abs(int(N)-100)
if M != 0:
    arr = list(input().split())

for i in range(1000001):
    stris = str(i)
    for stri in stris:
        if stri in arr:
            break
    else:
        result = min(result, abs(int(stris)-int(N))+len(stris))
        if int(stris) >= int(N):
            break

print(result)
