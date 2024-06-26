from collections import deque

n,m = map(int,input().split())
grid  = []
for _ in range (n):
    grid.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited = set()
q = deque([(0,0)])
visited.add((0,0))

def in_range (x,y):
    return 0<=x<n and 0<=y<m
answer = 0
while q:
    x,y =q.popleft()
    if (x,y) == (n-1,m-1):
        answer = 1
        break
    for i in range (4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx,ny) and grid[nx][ny] == 1 and not (nx,ny) in visited:
            q.append((nx,ny))
            visited.add((nx,ny))
print(answer)