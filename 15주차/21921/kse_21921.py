N, X = map(int, input().split())

blog = list(map(int, input().split()))

sum = sum(blog[:X])
max = sum
cnt = 1

for i in range(1, N-X+1):
    sum = sum - blog[i-1] + blog[i+X-1]
    if sum > max:
        _max = sum
        cnt = 0
    if max == sum:
        cnt += 1

print(max, cnt, sep="\n") if max else print("SAD")