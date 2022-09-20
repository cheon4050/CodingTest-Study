def solution(info, query):
    result = []
    optionList = [["cpp", "java", "python"], ["backend", "frontend"], ["junior", "senior"], ["chicken", "pizza"]]
    peopleDict = {}
    for a in ["cpp", "java", "python"]:
        for b in ["backend", "frontend"]:
            for c in ["junior", "senior"]:
                for d in ["chicken", "pizza"]:
                    peopleDict[a+b+c+d] = [0]*100001
    for s in info:
        s = s.split(" ")
        cnt = s.pop()
        s = "".join(s)
        peopleDict[s][int(cnt)] += 1
    for s in peopleDict:
        for i in range(1,100001):
            peopleDict[s][i] += peopleDict[s][i-1]
    for s in query:
        s = s.split(" and ")
        s[-1], cnt = s[-1].split(" ")
        cnt = int(cnt)
        temp = [s]
        for i in range(4):
            temp2 = []
            if temp[0][i] == "-":
                for s in temp:
                    for j in optionList[i]:
                        s[i] = j
                        temp2.append(s[:])
                temp = temp2[:]
        count = 0
        for s in temp:
            s = "".join(s)
            count += peopleDict[s][100000] - peopleDict[s][cnt-1]
        result.append(count)
    return result
