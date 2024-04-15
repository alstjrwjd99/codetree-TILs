n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs = [0,1,-1,0]
dys = [1,0,0,-1]

visited = [[0]*n for _ in range (n)]
global answer

def inrange(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global answer
    if visited[x][y] == 0:
        visited[x][y] = 1 
        answer += 1
        
    for i,j in zip(dxs,dys):
        nx = x + i
        ny = y + j
        if inrange(nx,ny) and grid[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            answer += 1
            dfs(nx,ny)

tmp = []
for i in range (n):
    for j in range (n):
        answer = 0
        if grid[i][j] == 1:
            dfs(i,j)
            if answer != 0:
                tmp.append(answer)
print(len(tmp))
tmp.sort()
for a in tmp:
    print(a)