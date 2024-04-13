n = int(input())
s1 = list(map(int,input().split()))
m = int(input())
s2 = list(map(int,input().split()))

tmpset = set(s1)
for a in s2:
    if a in tmpset:
        print(1,end = ' ')
    else :
        print(0,end = ' ')