K,N = map(int,input().split())
num=[i for i in range (1,K+1)]
answer = []
def dfs(numlist):
    if len(numlist) == N:
        print(*numlist)
        return
    for i in num:
        answer.append(i)
        dfs(answer)
        answer.pop()

dfs(answer)