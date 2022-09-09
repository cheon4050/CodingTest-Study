n = int(input())
num = 1
for i in range(1,n+1):
     num= num*i
str_num = str(num)
cnt = 0
for i in range(1,len(str(num))+1):
     if str_num[-i] != "0":
          break
     cnt+=1
print(cnt)