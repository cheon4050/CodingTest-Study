def solution(routes):
    answer = 0
    routes=sorted(routes,reverse=True) #일단 내림차순으로 정렬
    print(routes)
    
    while routes: #단속카메라에 해당되는 차는 없애줄거기때문에 routes가 빌 때까지 돌림
        start = routes[0][0]
        answer+=1
        temp = []
        for car in routes:
            if car[0] <= start and start <= car[1]: #예시로 들면 -10
                continue
            else:
                temp.append(car) #temp에 해당 차 정보를 넣는다.
                print(temp)
        routes = temp
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))