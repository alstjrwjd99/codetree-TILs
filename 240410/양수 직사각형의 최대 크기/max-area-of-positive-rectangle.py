n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range (n):
    for j in range (m):
        if grid[i][j] >0 :
            cnt = 0
            for x in range (i,n):
                for y in range (j,m):
                    if (grid[x][y]) > 0:
                        cnt +=1
                    else :
                        break
            answer = max(answer,cnt)
print(answer)