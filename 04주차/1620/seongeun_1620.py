n, m = map(int, input().split())
pocket_books = {}
#key는 포켓몬 이름, value는 입력 순서
for i in range(1, n+1):
    name = input().strip()
    pocket_books[name] = i

pocket_books_keys = list(pocket_books.keys()) #key만 모아 새로운 list를 생성

for _ in range(m):
    #입력이 isdigit()면 key를 출력하고 not isdigit()면 value를 출력
    name_or_number = input().strip()
    if name_or_number.isdigit():
        print(pocket_books_keys[int(name_or_number) - 1])
    else:
        print(pocket_books[name_or_number])
