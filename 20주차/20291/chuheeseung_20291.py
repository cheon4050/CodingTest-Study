def clean(n):
    answer = {}

    for _ in range(n):
        exe = input().split(".")[1] # 확장자만 분리
        answer.setdefault(exe, 0) # 확장자가 없으면 0으로 초기화 후 + 1
        answer[exe] += 1 # 확장자가 있으면 그냥 + 1

    for k, v in sorted(answer.items(), key = lambda x: x[0]): # 확장자 오름차순 정렬
        print(k, v)

n = int(input())
clean(n)