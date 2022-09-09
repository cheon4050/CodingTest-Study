n, m = map(int, input().split())
name = {} # 이름이 key인 딕셔너리
number = {} # 번호가 key인 딕셔너리
start = 1

for _ in range(n): # 포켓몬 이름이 순서대로 입력되면 그 순서가 포켓몬의 번호
    n = input()
    name[n] = start
    number[start] = n
    start += 1

for _ in range(m):
    question = input()

    if question.isnumeric():
        print(number[int(question)])
    else:
        print(name[question])