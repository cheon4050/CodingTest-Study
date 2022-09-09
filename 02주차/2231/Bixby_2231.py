n=int(input())
for i in range (n):
    if i+sum(map(int,list(str(i))))==n:
        break
print(i if i<n-1 else 0)