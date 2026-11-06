a, b = map(int, input().split())


# for i in range(a):
#     word += '*'

# for j in range(b):
#     print(word)

# word = ''

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()
    

# for j in range(b):
#     print(word)
# print(a, b)