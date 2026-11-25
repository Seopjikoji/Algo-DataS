def solution(n, lost, reserve):

    # 정렬, 리스트이기 때문에 sort() 함수 그냥 사용 가능
    lost.sort()
    reserve.sort()

    # lost 순회하면서 빌릴 수 있는지 판단
    for i in lost:
        if i in reserve:
            # reserve 에서만 빼주면 되고, 순회 중이니까
            target_index = reserve.index(i)
            del reserve[target_index]
            continue
        
        if i-1 in reserve:
            if i-1 in lost:
                n -= 1
                continue
            target_index = reserve.index(i-1)
            del reserve[target_index]
            continue

        if i+1 in reserve:
            if i+1 in lost:
                n -= 1
                continue
            target_index = reserve.index(i+1)
            del reserve[target_index]
            continue
        print(reserve)
        n -= 1

    return n

a = solution(5, [2, 3], [3, 4])
print(a)