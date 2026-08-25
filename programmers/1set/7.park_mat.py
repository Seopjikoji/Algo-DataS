def cal_range(x, y, max_x, max_y):
    if 0 <= x <= max_x and 0 <= y <= max_y:
        return True
    return False

def find_vaild_mats(mats, park, x, y, max_x, max_y):
    direction = ['NE', 'NW', 'SE', 'SW']
    asc_mats = sorted(mats)
    # print(asc_mats, 'asc_mats')
    mat_result = []
    # print(mat_result)
    for mat in asc_mats:
        # print(mat, 'mat 길이시작') 
        for d in direction:
            if d == 'NE':
                result = []
                for i in range(x, x + mat):
                    for j in range(y - mat + 1, y + 1):
                        # print(i, j, 'i, j', max_x, max_y, 'max_x, max_y', park[j][i], 'park[j][i]')
                        if cal_range(i, j, max_x, max_y):
                            if park[j][i] == '-1':
                                result.append('-1')
                # print('NE 방향 result:', result)
                if mat * mat == len(result):
                    mat_result.append(mat)
                    break
            elif d == 'NW':
                result = []
                for i in range(x - mat + 1, x + 1):
                    for j in range(y - mat + 1, y + 1):
                        if cal_range(i, j, max_x, max_y):
                            if park[j][i] == '-1':
                                result.append('-1')
                # print('NW 방향 result:', result)
                if mat * mat == len(result):
                    mat_result.append(mat)
                    break
            elif d == 'SE':
                result = []
                for i in range(x, x + mat):
                    for j in range(y, y + mat):
                        if cal_range(i, j, max_x, max_y):
                            if park[j][i] == '-1':
                                result.append('-1')
                # print('SE 방향 result:', result)
                if mat * mat == len(result):
                    mat_result.append(mat)
                    break
            elif d == 'SW':
                result = [] 
                for i in range(x - mat + 1, x + 1):
                    for j in range(y, y + mat):
                        if cal_range(i, j, max_x, max_y):
                            if park[j][i] == '-1':
                                result.append('-1')
                # print('SW 방향 result:', result)
                if mat * mat == len(result):
                    mat_result.append(mat)
                    break
    # print(mat_result)
    
    return max(mat_result) if mat_result else -1        
    
def solution(mats, park):

    answer = -1

    park_height = len(park)
    park_width = len(park[0])

    print(park_height, park_width, 'park_height, park_width')
    # 0에서 가로/세로 길이 -1(인덱스 고려해서)
    max_width_position = park_width - 1
    max_height_position = park_height - 1

    for i, v_1 in enumerate(park):
        for j, v_2 in enumerate(v_1):
            if v_2 == '-1':
                # print(j, i, 'TARGET j, i')
                #해당 돗자리르 순회하면서 깔 수 있는 돗자리인가 찾는 것
                answer = max(answer, find_vaild_mats(mats, park, j, i, max_width_position, max_height_position))

    return answer

answer = solution(
    [5,3,2],
    [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]
)

print (answer, 'answer')

