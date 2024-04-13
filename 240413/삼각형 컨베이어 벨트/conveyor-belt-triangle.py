n,t = map(int,input().split())
tri = []
for _ in range (3):
    tri.extend(list(map(int,input().split())))

def rotate():
    tmp = tri[-1]
    for i in range (n*3-1,-1,-1):
        tri[i] = tri[i-1]
    tri[0] = tmp

for i in range (t):
    rotate()

for idx, a in enumerate(tri):
    print(a,end=' ')
    if idx%3 ==2 :
        print()