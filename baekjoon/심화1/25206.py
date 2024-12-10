# 학점
markTotalScore = 0
# 학점 * 평점 
markmRateTotalScore = 0

def calRateByGradeScore(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4
    elif grade == 'B+':
        return 3
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2    
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1
    elif grade == 'D0':
        return 1.0
    else:
        return 0

# rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    A = input()
    mark = A.split(' ')[1]
    grade = A.split(' ')[2]

    if grade != "P":
        markTotalScore += float(mark)
        scoreByGrade = calRateByGradeScore(grade)
        
        markmRateTotalScore += float(mark) * scoreByGrade


print(markmRateTotalScore/markTotalScore)
