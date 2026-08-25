def convert_time_to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

def convert_seconds_to_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

def check_opening_time_and_calculate_position(op_start, op_end, pos):
    op_start_seconds = convert_time_to_seconds(op_start)
    op_end_seconds = convert_time_to_seconds(op_end)
    pos_seconds = convert_time_to_seconds(pos)

    if op_start_seconds <= pos_seconds <= op_end_seconds:
        return op_end_seconds
    else:
        return pos_seconds

def solution(video_len, pos, op_start, op_end, commands):
    video_len_seconds = convert_time_to_seconds(video_len)
    # pos_seconds = convert_time_to_seconds(pos)
    # op_start_seconds = convert_time_to_seconds(op_start)
    # op_end_seconds = convert_time_to_seconds(op_end)

    # 시작 위치 변수 선언
    video_location = 0

    # 기능 수행 전 오프닝 기간 범위 내인지 판단 > 시작 위치 정하기
    video_location = check_opening_time_and_calculate_position(op_start, op_end, pos)

    # 기능 수행 
    for command in commands:
        if command == "prev":
            video_location = max(0, video_location - 10)
        elif command == "next":
            video_location = min(video_len_seconds, video_location + 10)
        video_location = check_opening_time_and_calculate_position(op_start, op_end, convert_seconds_to_time(video_location))

    # # 기능 수행 후 오프닝 기간 범위 내인지 판단 > 종료 위치 정하기(마지막 기능 수행 후까지 판단하므로, 이후 오프닝 시간 검증 필요 없음)
    # if check_opening_time_and_calculate_position(op_start, op_end, convert_seconds_to_time(video_location)) == op_end_seconds:
    #     video_location = op_end_seconds
      
    return convert_seconds_to_time(video_location)

a = solution("07:22", "04:05", "00:15", "04:07", ["next"])
print(a, 'answer')  