n,m = map(int,input().split())
bomb  = []
for _ in range (n):
    bomb.append(int(input()))

explosion = [False] * n
answer = 0
for i in range (n):
    start = 0
    if i - m >= 0 :
        start = i-m
    if bomb[i] in bomb[start:i]:
        explosion[i] = True
    end = n
    if i+m < n:
        end = i+m+1
    if bomb[i] in bomb[i+1:end]:
        explosion[i] = True
    if explosion[i]:
        answer = max(answer,bomb[i])

print(answer) if answer !=0 else print(-1)