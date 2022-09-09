def is_placeable(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==x-i:
            return False
    return True
def dfs(x=0):
    global cnt
    if x==n:
        cnt+=1
    else:
        for i in range(n):
            row[x]=i
            if is_placeable(x):
                dfs(x+1)
n=int(input())
row=[0]*n
cnt=0
dfs()
print(cnt)