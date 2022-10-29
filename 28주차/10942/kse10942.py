n=int(input()) #수열의 크기
num_list= list(map(int, input().split())) # 홍준이가 칠판에 적은 수
m=int(input())
se_list=[]*m
for _ in range(m):
    se_list.append(list(map(int, input().split()))) # 홍준이가 명우에게 한 질문 SE

temp_list=' '.join(map(str,num_list))
# def _palindrome():

print(' '.join(map(str,num_list)))
print(se_list)
