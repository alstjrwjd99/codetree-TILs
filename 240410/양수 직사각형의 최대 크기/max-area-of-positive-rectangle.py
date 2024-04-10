n,m=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(n)]
result=-1

# 해당 구역 양수로 이루어져있는지 확인
def check(x,y,x2,y2):
    for i in range(x,x2+1):
        for j in range(y,y2+1):
            if array[i][j]<=0:
                return False
    return True


def make_rec(x,y,x2,y2):
    # 양수로 이루어져있으면
    if check(x,y,x2,y2):
        # 직사각형 최대 크기 줄력
        val=(abs(x-x2)+1)*(abs(y-y2)+1)
        return val
    return -1

# 값 체크할 직사각형 만들기
for x in range(n):
    for y in range(m):
       for x2 in range(x,n):
        for y2 in range(y,m):
            result=max(result,make_rec(x,y,x2,y2))

print(result)