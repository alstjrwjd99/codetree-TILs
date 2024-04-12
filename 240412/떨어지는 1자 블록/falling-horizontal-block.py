n,m,k = map(int,input().split())
k = k-1
grid = []
for _ in range (n):
    grid.append(list(map(int,input().split())))

# 2중 for문 돌면서 k,k+m-1 사이 1이 있는지 체크
def fall():
    for i in range (n-1):
        for j in range (k,k+m):
            if grid[i+1][j] == 1:
                for a in range (k,k+m):
                    grid[i][a] = 1
                return
fall()
for a in grid:
    print(*a)