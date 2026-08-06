def solution(wallet, bill):
    answer = 0

    wallet_min = min(wallet)
    wallet_max = max(wallet)
    bill_min = min(bill)
    bill_max = max(bill)
    # print(wallet_min, wallet_max, bill_min, bill_max, 'wallet_min, wallet_max, bill_min, bill_max')
    # print(wallet_min >= bill_min, wallet_max >= bill_max, 'wallet_min >= bill_min, wallet_max >= bill_max')


    while not (wallet_min >= bill_min and wallet_max >= bill_max):
        # print(wallet_min >= bill_min, wallet_max >= bill_max, 'wallet_min >= bill_min, wallet_max >= bill_max')
        # print('실행')
        # print(bill_min, bill_max, 'bill_min, bill_max')
        answer += 1
        folded = bill_max // 2
        remain = bill_min
        bill_min = min(folded, remain)
        bill_max = max(folded, remain)

        # print(wallet_min, wallet_max, bill_min, bill_max, 'wallet_min, wallet_max, bill_min, bill_max')
        # if bill_min == 0 or bill_max == 0:
        #     break
        
    return answer

a = solution([30, 15], [26, 17])
print(a, 'answer')