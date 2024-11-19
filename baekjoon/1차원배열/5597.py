all_regi_list = [i for i in range(1, 31)]
second_list = [i for i in range(1, 31)]

present_list = []

for i in range(1,29):
    A = int(input())
    present_list.append(A)

print(present_list)

for j in range(0,30):
    if all_regi_list[j] in present_list:
        second_list.remove(all_regi_list[j])

i=0
while i<2:
    print(second_list[i])
    i+=1
