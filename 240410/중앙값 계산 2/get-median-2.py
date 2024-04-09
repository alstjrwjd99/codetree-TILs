n = int(input())
answer = []
num = list(map(int,input().split()))
for idx in range (n+1):
    if idx % 2 == 1:
        answer.append(sorted(num[:idx])[idx//2])
print(*answer)