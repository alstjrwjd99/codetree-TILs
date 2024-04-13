import heapq

n,m = map(int,input().split())
s = list(map(int,input().split()))

hq  =[]
for i in s: 
    heapq.heappush(hq,-i)

for _ in range (m):
    hq[0] += 1
    heapq.heapify(hq)
print(hq[0]*(-1))