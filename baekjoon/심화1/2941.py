
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

total_cnt = 0

A = input()

for i in cro_list:
        if i in A:
            #   cro_cnt_list.append(A.count(i))
              total_cnt += A.count(i)
              A = A.replace(i, ' ')

print(A)                
B = A.replace(' ','')
print(total_cnt+len(B))

#공백으로 인해서 생기는 문제가 있었음. 캐치는 했는데 흠.. 아직 실력이 많이 부족하다. 조건을 잘 안봄
#dz=, z= 관련 조건을 잘못 해석했음. 문제를 잘 읽어야 함, 조건 수기로 써서 분리하는 연습, 문제를 유심히 읽고 충분히 고민
#기본기가 많이 부족하다 !, 값을 채워주는게 덜 헷갈리겠네
#아래는 좋은 코드

# a = input()
# croatia_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in croatia_a:
#     print(a)
#     a = a.replace(i, "*")

# print(a)
# print(len(a))
