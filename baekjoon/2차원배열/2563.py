n = int(input())

paper = [[0 for x in range(100)] for y in range(100)]


for i in range(n):
    x, y = map(int, input().split())
    for _x in range(x, x+10):
        for _y in range(y,y+10):
            if _x > 100 or _y > 100:
                break
            paper[_x][_y] = 1

sum = 0
for row in range(100):
    for each in range(100):
        if paper[row][each] == 1:
            sum += 1

print(sum)            
    

