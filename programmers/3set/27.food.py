def solution(food):

    # 좌측에서 시작
    left_food = ''

    for i, value in enumerate(food):
        if i !=0 and value != 1:
            print(i, value, value // 2)
            left_food += str(i) * (value // 2)

    # 역순, 좌측 대칭이 우측이니깐
    right_food = left_food[::-1]

    answer = left_food + '0' + right_food
    return answer

    # 코드 추천
    # # 음식점에서 제공하는 음식의 종류를 담은 리스트
    # food_list = []

    # # 음식 종류별로 반복하여 리스트에 추가
    # for i in range(len(food)):
    #     food_list.extend([str(i)] * (food[i] // 2))

    # # 음식 종류를 정렬하여 문자열로 변환
    # food_str = ''.join(sorted(food_list))

    # # 음식 문자열을 반으로 나누어 좌우 대칭을 만듦
    # left_half = food_str
    # right_half = food_str[::-1]

    # # 가운데에 0이 있는 경우 처리
    # middle = ''
    # for i in range(len(food)):
    #     if food[i] % 2 == 1:
    #         middle = str(i)
    #         break

    # # 최종 결과 문자열 생성
    # result = left_half + middle + right_half

    # return result

a = solution([1, 7, 1, 2])
print(a)