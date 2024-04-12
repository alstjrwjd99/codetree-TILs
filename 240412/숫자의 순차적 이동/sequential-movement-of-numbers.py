n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
def around_max(x,y):
    ans = 0
    coor = ()
    for i in range (8):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx,ny):
            if ans < grid[nx][ny]:
                ans = grid[nx][ny]
                coor = (nx,ny)
    return coor

def find(i):
    for a in range (n):
        for b in range (n):
            if grid[a][b] == i:
                coor = around_max(a,b)
                grid[a][b],grid[coor[0]][coor[1]] = grid[coor[0]][coor[1]],grid[a][b]
                return

for i in range (1,n**2+1):
    find(i)

for a in grid:
    print(*a)