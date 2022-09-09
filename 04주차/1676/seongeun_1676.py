N=int(input())
cnt, result=0,1

for i in range(N,1,-1):
    result*=i
for i in str(result)[::-1]: ## 처음부터 끝까지 -1칸 간격으로 ( == 역순으로)
    if i=='0':
        cnt+=1
    else:
        break
print(cnt)

# N = input()
# print(N//5 + N//25 + N//125)