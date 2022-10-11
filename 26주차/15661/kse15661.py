n = int(input()) #사람에게 정해진 번호

arr = []
for i in range(n):
    data = list(map(int, input().split())) #능력치 정보
    arr.append(data)

answer = int(1e9)
def dfs(index,first,second):
    global answer

    if index == n:
        st = 0 # start팀인지 구분
        li = 0 # link팀인지 구분

        # index의 사람을 start 팀에 넣었을 때
        for i in range(len(first)):
            for j in range(len(first)):
                if i != j:
                    st += arr[first[i]][first[j]]
        # index의 사람을 link 팀에 넣었을 때
        for i in range(len(second)):
            for j in range(len(second)):
                if i != j:
                    li += arr[second[i]][second[j]]

        answer = min(answer, abs(st-li))
        return

    dfs(index+1, first+[index], second)
    dfs(index+1, first, second+[index])

dfs(0,[],[])
print(answer)