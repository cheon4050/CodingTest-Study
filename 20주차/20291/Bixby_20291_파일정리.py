n = int(input())
dictionary = {}
for _ in range(n):
    name, extension = input().split('.')
    dictionary.setdefault(extension, 0)
    dictionary[extension] += 1
for e in sorted(dictionary.items()):
    print(*e)
