import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().rstrip()
    start, end = 0, len(s)-1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            break
    else:
        print(0)
        continue
    s1 = s[:start] + s[start+1:]
    s2 = s[:end] + s[end+1:]
    leftS1 = s1[:len(s)//2]
    rightS1 = s1[len(s)//2:][::-1]
    leftS2 = s2[:len(s)//2]
    rightS2 = s2[len(s)//2:][::-1]
    if len(leftS1) > len(rightS1):
        leftS1 = leftS1[:-1]
    elif len(leftS1) < len(rightS1):
        rightS1 = rightS1[:-1]
    if len(leftS2) > len(rightS2):
        leftS2 = leftS2[:-1]
    elif len(leftS2) < len(rightS2):
        rightS2 = rightS2[:-1]
    if leftS1 == rightS1:
        print(1)
        continue
    if leftS2 == rightS2:
        print(1)
        continue
    print(2)