n,m = map(int,input().split())
grid = []
for _ in range (n):
    grid.append(list(map(int,input().split())))

def check_line(line):
    cont = 1
    maxcnt = 1
    for i in range (1,n):
        if line[i] == line[i-1]:
            cont += 1
        else :
            cont = 1
        maxcnt = max(maxcnt,cont)
    return maxcnt >= m

answer = 0
for i in range (n):
    if check_line(grid[i]):
        answer +=1 
    if check_line([grid[j][i] for j in range (n)]):
        answer +=1 
print(answer)