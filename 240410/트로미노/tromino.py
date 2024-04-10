n,m = map(int,input().split())
maps = []
for i in range (n):
    maps.append(list(map(int,input().split())))

def check_nieun(x,y):
    if 0<=x and x+1 < n and 0<=y and y+1 < m:
        four = maps[x][y]+maps[x+1][y]+maps[x][y+1]+maps[x+1][y+1]
        return max(four - maps[x][y], four-maps[x+1][y],four-maps[x][y+1],four-maps[x+1][y+1])
    return 0

def check_long(x,y):
    if 0<=x and x+2 < n and 0<=y and y+2 < m:
        return max(maps[x][y]+maps[x][y+1]+maps[x][y+2],maps[x][y]+maps[x+1][y]+maps[x+2][y]) 
    return 0

answer = 0
for i in range (n):
    for j in range (m):
        answer = max(check_nieun(i,j),check_long(i,j),answer)
print(answer)