n,m = map(int,input().split())
bomb  = []
for _ in range (n):
    bomb.append(int(input()))

explosion = [False] * n
for i in range (n):
    start = 0
    if i - m >= 0 :
        start = i-m
    end = n
    if i+m < n:
        end = i+m+1
    if bomb[i] in bomb[start:i]+bomb[i+1:end]:
        explosion[i] = True
answer = 0
for idx,a in enumerate(explosion):
    if a :
        answer = max(answer,bomb[idx])
print(answer) if answer !=0 else print(-1)