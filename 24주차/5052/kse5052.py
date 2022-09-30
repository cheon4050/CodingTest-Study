#전화번호 목록이 주어진다. 이때 이 목록이 일관성이 있는지 없는지 확인하는

'''
1. 일관성을 유지하려면  한 번호가 다른 번호의 접두어인 경우가 없어야함.
ex)
긴급전화 : 911
상근 : 97 625 999
선영 : 91 12 54 26

이 경우 선영이에게 전화를 걸 수 있는 방법이 없음
선영이의 처음 번호 911을 누르자마자 긴급전화로 눌리기 때문
'''

N=int(input())
def solution(t,str_list):
    str_list=sorted(str_list) #작은 값부터 정렬
    for i in range(1, t):
        if str_list[i-1] == str_list[i][:len(str_list[i-1])]:
            print(len(str_list[i-1]))
            return "NO"
    return "YES"

for _ in range(N):
    str_list=[]
    t=int(input())
    for _ in range(t):
        str=input()
        str_list.append(str)
    print(solution(t, str_list))


'''
2
3
911
97825999
91125426

5
113
12340
123440
12345
98346
'''