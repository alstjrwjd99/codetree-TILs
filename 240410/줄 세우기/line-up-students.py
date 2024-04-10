n = int(input())
person = []
for i in range (1,n+1):
    tmp = tuple(map(int,input().split()))
    person.append((tmp[0],tmp[1],i))
person.sort(key = lambda x : (-x[0],-x[1],x[2]))
for a in person:
    print(*a)