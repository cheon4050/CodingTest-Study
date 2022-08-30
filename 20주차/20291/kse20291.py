#파일정리

n = int(input())
file = dict()

for _ in range(n) :
    e = (input().split('.'))[1] #확장자 처리
    if not e in file :
        file[e] = 1
    else :
        file[e] += 1

sort_file = sorted(file.items()) #sorted 메서드 활용

for key, value in sort_file :
    print(key.strip(), value)