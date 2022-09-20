from collections import deque

def solution(queue1, queue2):
    answer = -1
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)

    for i in range(300000): # 최대 길이가 300000
        if q1_sum == q2_sum:
            return i
        elif q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        else:
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num

    return answer # 값이 같아지지 않으면 -1 반환