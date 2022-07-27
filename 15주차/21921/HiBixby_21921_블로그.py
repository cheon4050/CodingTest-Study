n, x = map(int, input().split())
visited = list(map(int, input().split()))

cnt = 1
window = result = sum(visited[:x])
for start in range(n-x):
    window += visited[start+x]-visited[start]

    if window > result:
        cnt = 1
        result = window
    elif result == window:
        cnt += 1

if result > 0:
    print(result)
    print(cnt)
else:
    print("SAD")
