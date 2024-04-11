n,t = map(int,input().split())
tri = []
for _ in range (3):
    tri.append(list(map(int,input().split())))

def rotate():
    first_end = tri[0][-1]
    second_end = tri[1][-1]
    last_end = tri[2][-1]
    for j in range(3):
        tmp = tri[j][-1]
        for i in range (n-1,0,-1):
            tri[j][i]=tri[j][i-1]
    tri[0][0] = last_end
    tri[1][0] = first_end
    tri[2][0] = second_end

for i in range (t):
    rotate()
for a in tri:
    print(*a)