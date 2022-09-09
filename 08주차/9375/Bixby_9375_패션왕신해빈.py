for _ in range(int(input())):
    closet={}
    answer=1
    for _ in range(int(input())):
        clothes,type=input().split()
        closet[type]=closet.get(type,1)+1
    for type in closet:
        answer*=closet[type]
    print(answer-1)