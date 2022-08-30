N, K = list(map(int, input().split()))
datas = list(map(int, input().split()))

lenV = [0 for i in range(N)]
indexs = [[] for i in range(100001)]

popStartIndex = 0
count = 0

for i, data in enumerate(datas):
    if len(indexs[data])+1 > K: # 매핑된 배열이 2 초과일 때
        # print(indexs[data][0], count) # 2 (예를 들어 index[5]=[2,3,7] 이렇게 들어있을테니 )
        popLastIndex = indexs[data][0] # 맨 첨에 들어왔던 아이를 last indext로 두고
        for popIndex in range(popStartIndex, popLastIndex+1): #0부터 popLastIndex+1까지
            popVal = datas[popIndex] #
            indexs[popVal].pop(0)
            count -= 1 #같은 숫자가 3개 이상인 부분수열이므로 하나씩 빼주기
            print(count)
        popStartIndex = popLastIndex+1 #끝내고 나오기

    indexs[data].append(i) #각 data 인덱스에 매핑 해주기
    count += 1 #매핑 될때마다 1씩 올리기
    lenV[i] = count
print(max(lenV))