n = int(input())

start = [1,1,1,2,2]
for i in range(5, 100):
    start.append(start[i-1]+start[i-5])

for j in range(n):
    n = int(input())
    print(start[n-1])