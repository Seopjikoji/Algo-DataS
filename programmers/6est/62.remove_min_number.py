def solution(arr):

    # 길이가 1이면 [-1] return
    if len(arr) == 1:
        return [-1]
    else:
        # 길이가 2 이상일 경우 slicing 해서 배열 합치기
        # min_number = min(arr)
        # min_index = arr.index(min_number)
        # return arr[0:min_index] + arr[min_index+1:]

        # 다른 풀이
        arr.remove(min(arr))
        return arr
a = solution([4, 3, 2, 1])
print(a)