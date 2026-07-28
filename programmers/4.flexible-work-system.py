def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
      indpasscount = 0
      fixedday = startday
      for j in range(7):
        
        # print(startday, timelogs[i][j], schedules[i] + 10)
        if startday != 6 and startday != 7:
          if timelogs[i][j] <= schedules[i] + 10:
            indpasscount += 1
        
        # print(startday, i, 'S')
        startday += 1
        if startday == 8:
          startday = 1

      startday = fixedday
      print(startday, 'S')
      # print(indpasscount, 'I')        
      if indpasscount == 5:
        answer += 1 

    return answer

schedules = [700, 800, 1100]
timelogs = [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
startday = 5

a = solution(schedules, timelogs, startday)
print(a)