def solution(babbling):

    # 발음할 수 있는 단어 count
    count = 0

    # 발음할 수 있는 단어 리스트
    babbling_words = ["aya", "ye", "woo", "ma"]

    # 순회하면서, 단어를 읽어보기
    for word in babbling:

        index = 0
        before = ""
        # is_pass  = False
        # print(word, '시작')
        while index < len(word):
            print(index, word[index:], before, '/')
            is_pass = False
            # 발음할 수 있는 단어를 읽어보기
            for babbling_word in babbling_words:
                # 발음할 수 있는 단어인지 확인
                if word[index:index + len(babbling_word)] == babbling_word:
                    # 이전 단어와 같은 단어인지 확인
                    print(word[index:index + len(babbling_word)], before, babbling_word, before == babbling_word, '//')
                    if before == babbling_word:
                        is_pass = False
                        index = len(word)
                        break
                    is_pass = True
                    before = babbling_word
                    index += len(babbling_word)
                    break
                # else:
                #     is_pass = is_pass | False

            # print(is_pass)
            if not is_pass:
                # is_pass = False
                index = len(word)
                

            # index += 1
                # else:
                #     print('여기는 안오지 않나 ?')
                #     index += 1
        print(is_pass, index, len(word), '///')
        if index == len(word) and is_pass:
            count += 1

    return count

    # # 발음할 수 있는 단어 세기
    # count = 0

    # # 옹알이 단어
    # babbling_words = ["aya", "ye", "woo", "ma"]

    # # 단어 순회하면서, 발음할 수 있는 단어인지 아닌지 판단해야함. 문자열 내 순회는 in 으로 판단하면 좋을 것 같음
    # for word in babbling:
    #     for i in babbling_words:
    #         print(word, i)
    #         # 단어에 옹알이 단어가 2번 이상 반복되면 발음할 수 없는 단어임.
    #         if i * 2 not in word and i in word:
    #             word = word.replace(i, " ")

    #     if word.strip() == "":
    #         count += 1        
    # # 발음할 수 있는 단어 세기
    # count = 0

    # # 옹알이 단어
    # babbling_words = ["aya", "ye", "woo", "ma"]


    # for word in babbling:
    #     # stack 에 넣어보기
    #     stack = []
    #     before = ""
    #     # print('시작')
    #     print(word, '시작')
    #     print(stack, '시작')
    #     print(before, '시작')
    #     for i in word:
    #         # print(before)
    #         stack.append(i)
    #         print(stack)
    #         if len(stack) >= 3 and "".join(stack[-3:]) in babbling_words:
    #             print(before, '3')
    #             if before == "".join(stack[-3:]):
    #                 break
    #             before = "".join(stack[-3:])
    #             del stack[-3:]
    #         elif len(stack) >= 2 and "".join(stack[-2:]) in babbling_words:
    #             print(before, '2')
    #             if before == "".join(stack[-2:]):
    #                 break
    #             before = "".join(stack[-2:])
    #             del stack[-2:]


    #     if len(stack) == 0:
    #         print(stack, 'answer')
    #         count += 1

    #     # print(stack)    
    #     stack = []
    #     before = ""
          
    # for word in babbling:
    #     for i in ["aya", "ye", "woo", "ma"]:
    #         if i * 2 not in word:
    #             word = word.replace(i, " ")
    #     if word.strip() == "":
    #         answer += 1
    # return count

a = solution(["aya", "yee", "u"])
print(a)