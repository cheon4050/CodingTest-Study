#투에-모스 문자열
#k - 1번 째부터 절반씩 줄여나가며, 2의 배수일 때만 문자를 뒤바꿔줌
k = int(input())
ans=0
k=k-1
while k:
    ans+=k%2
    k//=2
print(abs(ans%2))