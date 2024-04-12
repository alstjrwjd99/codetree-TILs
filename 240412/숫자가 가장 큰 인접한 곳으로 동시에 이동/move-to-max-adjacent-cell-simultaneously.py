n, m, t = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
biz = []
for _ in range(m):
    r,c = list(map(int, input().split()))
    biz.append((r-1,c-1))   

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move(biz):
    for idx,b in enumerate(biz):
        max_value = 0
        for i in range (4):
            nx = b[0] + dx[i]
            ny = b[1] + dy[i]
            if in_range(nx,ny):
                if grid[nx][ny] > max_value:
                    max_value = grid[nx][ny]
                    biz[idx] = (nx,ny)
    dup = [[0]*n for _ in range (n)]
    tmp = []
    for idx,b in enumerate(biz):
        dup[b[0]][b[1]] += 1
    for i in range (n):
        for j in range (n) :
            if (dup[i][j]) == 1:
                tmp.append((i,j))                
    return tmp

for _ in range (t):
    biz = move(biz)
print(len(biz))