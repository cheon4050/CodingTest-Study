words_list = []
words_set = []
n = int(input())
words_list = list(input() for _ in range(n))

for i in words_list:
    if i not in words_set:
        words_set.append(i)

words_set.sort()
words_set.sort(key=len)

for i in words_set:
    print(i)