n = int(input())
person = []
for i in range (1,n+1):
    tmp = tuple(map(int,input().split()))
    person.append(( abs(tmp[0])+abs(tmp[1]),i ))
person.sort()
for a in person:
    print(a[1])