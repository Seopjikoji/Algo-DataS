def solution(a, b, n):

  # 남은 콜라 개수가 a 보다 작아질 때까지 새로 받은 콜라 빈 병 만들고, 갖다 주는 행위 반복
  # 남은 콜라 개수와 몇 병을 받을 수 있는지를 나타내는 변수가 필요
  remain = n
  count = 0

  while remain >= a:
      # 새로 받은 콜라 개수 계산
      new = (remain // a) * b
 
      # 새로 받은 콜라 count 에 더해주기
      count += new

      # 나머지 콜라 개수 계산(새로 받은 콜라 개수 반영)
      remain = remain - ((remain // a) * a) + new

  return count

a = solution(3, 2, 20)
print(a)