target_list = [3, 1, 2, 4]

#선택정렬 오름차순
for i in range(len(target_list)):
    min_index = i
    for j in range(i+1, len(target_list)):
        if target_list[min_index] > target_list[j]:
            min_index = j
    target_list[i], target_list[min_index] = target_list[min_index], target_list[i]

print(target_list)

#선택정렬 내림차순
# for i in range(len(target_list)):
#     max_index = i
#     for j in range(i+1, len(target_list)):
#         if target_list[max_index] < target_list[j]:
#             max_index = j
#     target_list[i], target_list[max_index] = target_list[max_index], target_list[i]

# print(target_list)