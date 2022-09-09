w = [input() for i in range(int(input()))]
w = list(set(w))
w.sort(key= lambda x : (len(x), x))
print('\n'.join(w))