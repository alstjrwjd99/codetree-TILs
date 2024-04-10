n = int(input())
person = []
for i in range (1,n+1):
    person.append(input().split())
person.sort(key = lambda x : (int(x[1]), -1 * int(x[2])))
for a in person:
    print(*a)