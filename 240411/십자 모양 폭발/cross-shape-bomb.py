n = int(input())
grid = []
for _ in range (n):
    grid.append(list(map(int,input().split())))
x,y = map(int,input().split())
x -= 1
y -= 1
dx,dy = [-1,1,0,0],[0,0,1,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def explosion(x,y):
    ret = [(x,y)]
    boundry = grid[x][y]
    for i in range (4):
        nx = x + dx[i]
        ny = y + dy[i]
        for _ in range (boundry-1):
            if in_range(nx,ny):
                ret.append((nx,ny))
                nx += dx[i]
                ny += dy[i]
            else :
                break
    return ret

def fall(grid):
    for j in range (n):
        tmp = []
        start = 0
        for i in range (n-1,-1,-1):
            if grid[i][j] == 0:
                start = i
            if start and grid[i][j] != 0 :
                tmp.append(grid[i][j])
                grid[i][j] = 0
        for idx, a in enumerate (tmp):
            grid[start][j] = a
                    
for coor in (explosion(x,y)):
    grid[coor[0]][coor[1]] = 0

fall(grid)

for a in grid:
    print(*a)