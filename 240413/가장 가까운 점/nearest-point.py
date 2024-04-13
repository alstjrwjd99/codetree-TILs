import heapq

n,m = map(int,input().split())
coor = []
for _ in range (n):
    x,y = map(int,input().split())
    heapq.heappush(coor,((abs(x)+abs(y)),x,y))
for _ in range (m):
    tmp = heapq.heappop(coor)
    heapq.heappush(coor,((abs(tmp[1]+2)+abs(tmp[2]+2)),tmp[1]+2,tmp[2]+2))
a = heapq.heappop(coor)
print(a[1],a[2])