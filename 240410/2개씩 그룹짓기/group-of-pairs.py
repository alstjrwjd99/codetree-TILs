n = int(input())
a = list(map(int,input().split()))
a.sort()
answer = 0
for i in range (n):
    answer = max(a[i]+a[n*2-i-1],answer)
print(answer)