S= input().split('-');

sum = 0
for i in S[0].split('+'):
    sum+=int(i)

for i in S[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)