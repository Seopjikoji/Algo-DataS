def solution(numbers):
    # 한번에(2번째 아이디어)
    # return 45 - sum(numbers)

    compare_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # numbers 순회하면서 pop 생각함
    for i in numbers:
        if i in compare_list:
            compare_list.remove(i)

    return sum(compare_list)

a = solution([5,8,4,0,6,7,9])
print(a)