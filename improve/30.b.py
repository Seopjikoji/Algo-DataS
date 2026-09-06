def solution(babbling):

    # 발음할 수 있는 단어
    pronounceable_word = ['aya', 'ye', 'woo', 'ma']

    # 발음할 수 있는 단어 count
    count = 0

    # 테스트 단어들을 순회하면서, 해당 발음을 발음할 수 있는지 체크해야함
    # 문제 처음 풀었을 때는, 해당 문자열에 이 문자열이 있는지 확인하는 in 방식이 생각나지 않았음
    # 이 for 문의 시간 복잡도는 빅오 표기법으로, 최대 100

    for word in babbling:
        # 이 문자열을 발음할 수 있는지 인덱스 0부터 시작해서 체크해야함
        # 단어마다 초기화 해야하기 때문에 for문 내 초반부에 적어준다
        index = 0
        before = ''
        # 해당 단어를 체크하는 도중에 발음이 읽을 수 없다고 생각하는 순간 해당 단어 다음 단어로 넘어갈 수 있도록 해야함
        # 단어 전체를 순회하지만, 규칙적으로 순회하지 않고, index를 자유롭게 이동시켜야 하므로, for 문 보다는 while 문으로 반복문을 작성하도록 한다. 까다로운 건 사실..
        # while 문이 끝나는 시점은, 이 단어가 읽을 수 없는 단어이거나, 끝까지 단어를 다 읽었을 때
        # 시간 복잡도는 word 의 길이, 문제 조건에서 최대 30

        # 다음 index 회차로 넘어갈건지를 판단하는 변수 pass 여부를 기억해서 while 문도 벗어 날 수 있게 하면 좋을 듯, while 문 바깥에 있어야, while 문 끝나고 나서, count 할 수 있음
        is_pass = False
        
        while index < len(word):
            # 발음할 수 있는 단어들을 순회하면서, 하나라도 맞으면 그 자체로 for 문을 끝내고 다음 index 로 넘어가면 됨. for 문을 다 돌았는데도 없으면 다음 단어로 넘어가면 됨
            # 연속해서 발음을 할 수 없기 때문에 이전에 발음 성공한 단어를 기억해야함, while 문 바깥에 둘거냐 안에 둘거냐를 생각해보면 밖에 둬야 while 문이 다시 돌 때 초기화되지 않음
            # 밑에 for 문 시간 복잡도는 4, 최종적으로 최악 100 * 30 * 4 해도 1억 안넘어 가기 때문에, 풀이에 지장을 주는 문제가 아님. 그냥 세부적인 부분을 코드로 표현할 수 있는지를 평가하는 문제 같음.
            is_pass = False
            
            for p in pronounceable_word:
                # print(word, before, p)
                if word[index:index+len(p)] == p and before !=p:
                    # print(word, p, 'IN')
                    index += len(p)
                    before = p
                    is_pass = True
                    break
            print(word, is_pass)
            # pass 못하면 그냥 while 문도 끝내면 됨
            if not is_pass:
                # is_pass = False
                break
        
        if is_pass:
            count += 1

    return count
    
a = solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
print(a)