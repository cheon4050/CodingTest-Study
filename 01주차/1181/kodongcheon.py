N = int(input())

wordList = []
for i in range(N):
    word = input()
    if word in wordList:
        continue
    wordList.append(word)

wordList = sorted(wordList, key= lambda x : (len(x), x))
for word in wordList:
    print(word)