n,m = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range (n)
]

dxs = [0,1]
dys = [1,0]

visited = [[0]*m for _ in range (n)]
global answer
answer = 0

def inrange(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    global answer
    if (x,y) == (n-1,m-1):
        answer = 1
        return 
    for i,j in zip (dxs,dys):
        nx = x + i
        ny = y + j
        if inrange(nx,ny) and grid[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx,ny)

visited[0][0] = 1
dfs(0,0)

print(answer)