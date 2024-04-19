n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range (n)
]
dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def in_range (x,y):
    return 0<=x<n and 0<=y<n

visited = set()
global answer,block
answer = []
block = 0

def dfs(x,y,cnt):
    global answer,block
    if cnt > 3:
        answer.append(cnt)
    for dx,dy in zip (dxs,dys):
        nx = dx + x
        ny = dy + y
        if in_range(nx,ny) and grid[x][y]==grid[nx][ny] and (nx,ny) not in visited:
            visited.add((nx,ny))
            cnt += 1
            dfs(nx,ny,cnt)
    return cnt

for i in range (n):
    for j in range (n):
        if (i,j) not in visited:
            count = dfs(i,j,0)  
            if count > 0:
                block += 1

print(block, max(answer))