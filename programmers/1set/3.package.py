def solution(n, w, num):
    answer = 0
    package_locaiton = []
    x = 0
    y = 1

    for i in range(n):
        if i % w == 0 and i != 0:
            y += 1
            package_locaiton.append((x, y))
        else:
            x += 1 if y % 2 != 0 else -1
            package_locaiton.append((x, y))

    target_package_x = package_locaiton[num - 1][0]
    target_package_y = package_locaiton[num - 1][1]

    target_package_max_y = max(b for a, b in package_locaiton if a == target_package_x)

    # print(target_package_x, target_package_max_y)

    # print(package_locaiton)
    answer = target_package_max_y - target_package_y + 1
    return answer

a = solution(13, 3, 6)

print(a)
