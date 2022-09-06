n = int(input())
arr = list(map(int,input().split()))

#실수하는 횟수 누적 합
answer = [0]
mistake = 0
for i in range(1, n):
    if (arr[i-1] > arr[i]): # 지금 연주하는 악보가 다음 악보보다 어려울 때
        mistake += 1
    answer.append(mistake)

q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    print(answer[y-1]- answer[x-1])