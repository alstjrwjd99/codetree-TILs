n,m = map(int,input().split())
maps = []
for _ in range (n):
    maps.append(list(map(int,input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 마름모 모양 만들기
def rhombus(x,y,k):
    k += 1
    visited = set()
    for i in range (k):
        for j in range (i):
            if in_range(x-k+i,y-j):
                visited.add((x-k+i,y-j))
            if in_range(x-k+i,y+j):
                visited.add((x-k+i,y+j))
            if in_range(x+k-i,y-j):
                visited.add((x+k-i,y-j))
            if in_range(x+k-i,y+j):
                visited.add((x+k-i,y+j))
        if in_range(x,y-i):
            visited.add((x,y-i))
        if in_range(x,y+i):
            visited.add((x,y+i))
    return list(visited)

# 범위내 골드 값 구하기
# 골드 값 - 마름모 수고비 > 0 인 부분
def total(x,y,k):
    earn = 0
    for a in (rhombus(x,y,k)):
        if maps[a[0]][a[1]] == 1:
            earn += 1
    if (earn*m - (k**2+(k+1)**2)) >= 0:
        return earn
    return 0

answer = 0
for i in range (n):
    for j in range (n):
        for k in range (20):
            answer = max(answer,total(i,j,k))
print(answer)