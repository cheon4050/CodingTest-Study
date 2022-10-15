from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
member_list = list(i for i in range(n))
score_map = []
ans = 10 ** 8

for _ in range(n):
    score_map.append(list(map(int, input().split())))

for i in range(1, int((n/2) + 1)):
    member_divide = combinations(member_list, i) # 팀을 나누기 위한 조합을 구함
    min_diff = 10 ** 8

    for x in member_divide:
        start_list = list(x)
        link_list = list(set(member_list) - set(start_list)) # 전체에서 스타트팀을 뺀 인원을 링크팀에 넣음
        start_all_sum = 0
        link_all_sum = 0

        for i in range(n - 1):
            for j in range(n - 1):
                try: # 스타트팀의 능력치를 구함
                    start_sum = score_map[start_list[i]][start_list[j]]
                except IndexError:
                    start_sum = 0

                try: # 링크팀의 능력치를 구함
                    link_sum = score_map[link_list[i]][link_list[j]]
                except IndexError:
                    link_sum = 0

                start_all_sum += start_sum
                link_all_sum += link_sum

        diff = abs(start_all_sum - link_all_sum) # 능력치의 최솟값을 구하기
        min_diff = min(min_diff, diff)

    ans = min(ans, min_diff)

print(ans)