# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

#index를 1번 부터 사용하기 위해 n+1만큼 할당합니다.
graph = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]

rel = []
for _ in range (m):
    rel.append(list(map(int,input().split())))

for r in rel :
    graph[r[0]][r[1]] = 1
    graph[r[1]][r[0]] = 1

global answer
answer = 0
def dfs(vertex):
    global answer

    for i in range (1,n+1):
        if graph[vertex][i] == 1 and not visited[i]:
            visited[i] = True
            answer+=1
            dfs(i)
visited[1] =True
dfs(1)
print(answer)