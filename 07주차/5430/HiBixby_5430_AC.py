from collections import deque
for _ in range(int(input())):
    c=input()
    n=int(input())
    q=deque(eval(input()))
    try:
        step=1
        for p in c:
            if p=="R":
                step*=-1
            else:
                q.popleft() if step==1 else q.pop()
        print(str(list(q)[::step]).replace(" ",""))
    except:
    	print('error')