n = int(input())
mirror = []
for _ in range (n):
    mirror.append(input())
start = int(input())

# 0,3 1,2 이렇게 한쌍
dx,dy = [1,0,-1,0],[0,-1,0,1]

# x, y, direct
def init_point(start):
    if start <= n:
        return (0,start-1,0)
    elif start <= 2*n:
        return (start-n-1,n-1,1)
    elif start <= 3*n:
        return (n-1,3*n-start,2)
    elif start <= 4*n:
        return (4*n - start,0,3)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def move(x,y,direct):
    x += dx[direct]
    y += dy[direct]
    return (x,y,direct)

def simulate(x,y,move_dir):
    move_num = 0
    while in_range(x,y):
        # 0,1   2,3
        if mirror[x][y] == '/':
            x,y,move_dir = move(x,y,move_dir ^ 1)
        # 0,3   1,2
        else :
            x,y,move_dir = move(x,y,3-move_dir)
        
        move_num += 1
    return move_num

x, y, direct = init_point(start)
print(simulate(x,y,direct))