from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    mid = (queue1_sum + queue2_sum) //2
    count = 0
    for i in range(len(queue1)*3):
        num = 0
        if queue1_sum == mid:
            break
        elif queue1_sum < mid:
            num = queue2.popleft()
            queue1.append(num)
            queue1_sum += num
            queue2_sum -= num
            count += 1
        else:
            num = queue1.popleft()
            queue2.append(num)
            queue2_sum += num
            queue1_sum -= num
            count += 1
    else:
        return -1
    return count