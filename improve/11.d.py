target_list = [3, 1, 2, 4]

def sort_asc(target_list):
    #선택정렬 오름차순
    for i in range(len(target_list)):
        min_index = i
        for j in range(i+1, len(target_list)):
            if target_list[min_index] > target_list[j]:
                min_index = j
        target_list[i], target_list[min_index] = target_list[min_index], target_list[i]
    return target_list

asc_list = sort_asc(target_list)
print(asc_list, 'asc')

def sort_desc(target_list):
    #선택정렬 내림차순
    for i in range(len(target_list)):
        max_index = i
        for j in range(i+1, len(target_list)):
            if target_list[max_index] < target_list[j]:
                max_index = j
        target_list[i], target_list[max_index] = target_list[max_index], target_list[i]
    return target_list

desc_list = sort_desc(target_list)
print(desc_list, 'desc')