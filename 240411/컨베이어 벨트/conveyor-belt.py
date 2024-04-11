n,t = map(int,input().split())
belt = []
for _ in range (2):
    belt.append(list(map(int,input().split())))

def rotate():
    first_end = belt[0][-1]
    second_end = belt[1][-1]
    for i in range (n-1,0,-1):
        belt[0][i] = belt[0][i-1]
    for i in range (n-1,0,-1):
        belt[1][i] = belt[1][i-1]
    belt[1][0] = first_end
    belt[0][0] = second_end
for _ in range (t):
    rotate()

for a in belt:
    print(*a)