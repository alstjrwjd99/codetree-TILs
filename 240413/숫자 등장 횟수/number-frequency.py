from collections import Counter

n,m = map(int,input().split())
num = list(map(int,input().split()))
find = list(map(int,input().split()))

c = Counter(num)
for f in find:
    print(c[f],end = ' ')