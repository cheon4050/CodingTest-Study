
from itertools import combinations

N, M = map(int, input().split())
li = []
for i in range(1,N+1):
    li.append(i)

for l in list(combinations(li, M)):
    for i in l:
        print(i,end=' ')
    print()



# check=[0]*(n+1)
# t=[0]*m
#
# def make(n, m, l):
#     if l==m:
#         for i in range(m):
#             print (t[i], end=' ')
#         print()
#         return
#
#     for i in range(1, n+1):
#         if check[i]==0:
#             t[l]=i
#             for j in range(i+1):
#                 check[j]=1
#             make(n,m,l+1)
#             for k in range(i+1):
#                 check[k]=0
#
# make(n,m,0)