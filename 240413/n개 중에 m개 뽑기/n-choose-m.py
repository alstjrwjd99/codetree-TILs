n,m = map(int,input().split())
num = []

def dfs(num,s):
    if len(num) == m:
        print(*num)
        return
    
    for i in range (s,n+1):
        num.append(i)
        dfs(num,i+1)
        num.pop()
dfs(num,1)