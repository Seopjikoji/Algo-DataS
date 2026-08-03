def cal_accepted_schedule_time(schedule):
    hour = schedule // 100
    minute = schedule % 100

    if minute + 10 >= 60:
        hour += 1
        minute = (minute + 10) % 60
    else:
        minute += 10
    
    return hour * 100 + minute
    

def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        indpasscount = 0
        fixedday = startday
        a = cal_accepted_schedule_time(schedules[i])
        print(a)
        for j in range(7):
            # print(startday, timelogs[i][j], schedules[i] + 10)
            if startday != 6 and startday != 7:
                if timelogs[i][j] <= cal_accepted_schedule_time(schedules[i]):
                    indpasscount += 1
        
            # print(startday, i, 'S')
            startday += 1
            if startday == 8:
                startday = 1

        startday = fixedday
        # print(startday, 'S')
        print(indpasscount, 'I')        
        if indpasscount == 5:
            answer += 1 

    return answer

schedules = [730, 855, 700, 720]
timelogs = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
startday = 1

a = solution(schedules, timelogs, startday)
print(a, 'answer')