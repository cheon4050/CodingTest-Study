n=int(input()) #센서의 길이
k=int(input()) #집중국의 개수
sensor_list= list(map(int, input().split())) #센서의 좌표

#총 18분 걸림

sensor_list=sorted(sensor_list)
temp_min=[]
for i in range(1, n):
    temp_min.append(sensor_list[i]-sensor_list[i-1])

temp_min=sorted(temp_min)
temp=temp_min[:(n-k)] # N개의 센서들을 k개의 묶음으로 묶었을 때 필요한 차이값의 개수가 n-k이므로 그만큼 차이값이 들어있는 리스트에서 잘라주면 됨.
print(sum(temp))