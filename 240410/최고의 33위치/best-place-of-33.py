n = int(input())
grid = []
for _ in range (n):
    grid.append(list(map(int,input().split())))

def in_range(x,y):
    return 0<=x and x+2<n and 0<=y and y+2<n

def count_coin(x,y):
    coins = 0
    for i in range (3):
        for j in range (3):
            if grid[x+i][j] == 1:
                coins += 1
    return coins

answer = 0 
for i in range (n):
    for j in range (n):
        if in_range(i,j):
            answer += count_coin(i,j)
print(answer)