n = int(input())
meeting = [] # 회의 시작, 종료 시간을 저장하는 리스트
room = 0
meeting_count = 0

for _ in range(n):
    start, end = map(int, input().split()) # 회의 시작, 종료 시간 입력 받음
    meeting.append([start, 1]) # 시작 시간은 1과 함께 추가
    meeting.append([end, -1]) # 종료 시간은 -1과 함께 추가

meeting.sort() # 리스트 정렬

for _, state in meeting: # state는 1, -1 둘 중 하나
    meeting_count = meeting_count + state
    # meeting_count 값이 시작에는 올라가고 종료에는 내려간다
    # state 값이 1에서 -1로 넘어가니까 결국 meeting_count는 0으로 돌아오게 된다 <- 회의는 어쨌든 종료하니까
    room = max(meeting_count, room) # 이용한 회의실의 개수를 업데이트
    # meeting_count의 최댓값 = 최소 회의실 개수

print(room)