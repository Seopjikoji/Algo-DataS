def cal_keypad_distance(keypad, input, number):
        
    # 현재 숫자 좌표 초기화
    num_y, num_x = 0, 0

    # 왼손 좌표 초기화
    hand_y, hand_x = 0, 0

    # 현재 숫자 좌표
    for y in range(4):
        for x in range(3):
            if keypad[y][x] == input:
                num_y, num_x = y, x

    # 손 위치
    for y in range(4):
        for x in range(3):
            if keypad[y][x] == number:
                hand_y, hand_x = y, x

    # print(f'현재 숫자: {i}, 좌표: ({num_y}, {num_x})')
    # print(f'왼손 좌표: ({left_y}, {left_x}), 오른손 좌표: ({right_y}, {right_x})')
    
    return abs(num_y - hand_y) + abs(num_x - hand_x)

def solution(numbers, hand):

    # 정답
    result = []

    # 키패드
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]

    # 손 위치
    left = '*'
    right = '#'

    # numbers 순회하면서 L 반환할지 R 반환할지 판단
    for i in numbers:
        if i in [1, 4 ,7]:
            result.append('L')
            left = i
        elif i in [3, 6, 9]:
            result.append('R')
            right = i
        else:
            left_distance = cal_keypad_distance(keypad, i, left)
            right_distance = cal_keypad_distance(keypad, i, right)
            
            if left_distance == right_distance:
                if hand == 'left':
                    result.append('L')
                    left = i
                else:
                    result.append('R')
                    right = i
            else:
                if left_distance < right_distance:
                    result.append('L')
                    left = i
                else:
                    result.append('R')
                    right = i

    return ''.join(result)

a = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
print(a)
