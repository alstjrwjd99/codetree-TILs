n,r,c = map(int,input().split())
r,c = r-1,c-1
grid = []
for _ in range (n):
    grid.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

answer = [(r,c)]
while True:
    run = False
    for i in range (4):
        nx = r + dx[i]
        ny = c + dy[i]
        if in_range(nx,ny):
            if grid[nx][ny] > grid[r][c]:
                r,c, = nx,ny
                answer.append((r,c))
                run = True
                break
    if not run :
        break
for a in answer:
    print(grid[a[0]][a[1]],end = ' ')