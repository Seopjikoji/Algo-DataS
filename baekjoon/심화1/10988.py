A = input()

check = ''

for i in range(len(A)//2):
    if A[i] != A[-1-i]:
        check+='0'
    else:
        check+='1'

if check.find('0') == -1:
    print(1)
else:
    print(0)

#더 괜찮은 풀이

# word = input()
# for i in range(len(word)//2):
#     if word[i] == word[-1-i]:
#         pass
#     else:
#         print(0)
#         exit(1)

# print(1)
# print(word)
# print(word[::-1])
        
# if word == word[::-1]:
#     print(1)
# else:
#     print(0)

# word = list(input())
# reversed_word = list(reversed(word)
#                      )
# print(word)
# print(reversed(word))

# if word == reversed_word :
#     print(1)
# else :
#     print(0)

# if word == test_word:
#     print('test')
# else:
#     print('test2')

# word2 = list(input())
# word_reverse = list(reversed(word2))

# if word == word_reverse :
#     print(1)
# else :
#     print(0)

