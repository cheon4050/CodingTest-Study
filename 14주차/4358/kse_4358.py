trees ={}
c =0
while True:
    t = input().strip()
    if len(t) ==0:
        break
    if t not in trees:
        trees[t] = 1
    else:
        trees[t] +=1
    c+=1

# 딕셔너리 key 정보를 정렬 시켜서 순서대로 출력되게 조건을 마련한다.
trees_sort = sorted(trees.keys())
for name in trees_sort:
    val = round(trees[name]/c *100,4)
    # 소수점 네번째까지 문자열로 나타내야 해서 format 함수를 사용해 나타냈다.
    print("{} {:.4f}".format(name,val))