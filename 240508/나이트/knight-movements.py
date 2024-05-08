from collections import deque

n = int(input())
r1,c1,r2,c2 = tuple(map(int,input().split()))
dxs = [-1,-2,-2,-1,1,2,2,1]
dys = [-2,-1,1,2,2,1,-1,-2]

queue = deque([(r1-1,c1-1,0)])

def bfs():
    while queue:
        x,y,z = queue.popleft()
        if (x,y) == (r2-1,c2-1):
            return z
        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0<= ny < n :
                queue.append((nx,ny,z+1))
    return -1

print(bfs())