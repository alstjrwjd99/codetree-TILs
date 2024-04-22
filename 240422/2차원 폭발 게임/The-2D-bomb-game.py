from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
bomb = [
    list(map(int,input().split()))
    for _ in range (n)
]

def rotate(bomb):
    copy = [[0] * n for _ in range (n)]
    for i in range (n):
        for j in range (n):
            copy[j][i] = bomb[n-1-i][j] 
    for i in range (n):
        for j in range (n):
            bomb[i][j] = copy[i][j]
    return bomb

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(x,y):
    start = bomb[x][y]
    queue = deque([(x,y)])
    dxs = [-1,1]
    dys = [0,0]
    tmp = set()
    tmp.add((x,y))
    while queue:
        a,b = queue.popleft()
        for dx,dy in zip(dxs,dys):
            nx = a + dx
            ny = b + dy
            if in_range(nx,ny) and start == bomb[nx][ny] and (nx,ny) not in tmp:
                tmp.add((nx,ny)) 
                queue.append((nx,ny))
    if len(tmp) >= m:
        return tmp                   
    else :
        return []       

def explose(bomb):
    for i in range (n):
        for j in range (n):
            if bomb[i][j]:
                will_bomb = bfs(i,j)
                if len(will_bomb) != 0:
                    for bombs in will_bomb :
                        bomb[bombs[0]][bombs[1]] = 0
    return bomb
    
def fall(bomb):
    copy = [[0] * n for _ in range (n)]
    for i in range (n):
        pointer = n-1
        for j in range (n-1,-1,-1):
            if bomb[j][i] :
                copy[pointer][i] = bomb[j][i]
                pointer -=1
    bomb = copy
    return bomb


for _ in range (k):
    bomb = explose(bomb)
    bomb = fall(bomb)
    bomb = rotate(bomb)
    bomb = fall(bomb)

answer = 0
for i in range (n):
    for j in range (n):
        if bomb[i][j]:
            answer += 1
print(answer)