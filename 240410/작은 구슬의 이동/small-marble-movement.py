n,t = map(int,input().split())
r,c,d = input().split()
r,c = int(r),int(c)
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

direct = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
    }

def in_range(x,y):
    return 0<x<n and 0<y<n
i = direct[d]
for _ in range (t):
    nx = r + dxs[i]
    ny = c + dys[i]
    if not in_range(nx,ny):
        i = 3-i
        continue
    r,c = r +dxs[i], c+dys[i]
print(r,c)