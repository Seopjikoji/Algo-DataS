all_regi_list = [i for i in range(1, 31)]

#두번째
for i in range(28):
    A = int(input())
    all_regi_list.remove(A)

print(all_regi_list[0])
print(all_regi_list[1])
#첫번째
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

