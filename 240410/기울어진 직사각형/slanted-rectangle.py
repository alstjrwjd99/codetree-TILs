n = int(input())
maps = []
for _ in range (n):
    maps.append(list(map(int,input().split())))

dx = [-1,-1,1,1]
dy = [1,-1,-1,1]

def in_range(x,y):
    return 0<= x<n and 0<= y<n

def bingle (x,y):
    sums = 0
    for i in range (4):
        cnt = 0
        while in_range(x,y):
            cnt += 1
            sums += maps[x][y]
            x += dx[i]
            y += dy[i]
        x -= dx[i]
        y -= dy[i]
        sums -= maps[x][y]
        if cnt <= 1:
            return 0
    return sums

answer = 0
for i in range (n):
    for j in range (n):
        if bingle(i,j) > answer:
            answer = bingle(i,j)
print(answer)