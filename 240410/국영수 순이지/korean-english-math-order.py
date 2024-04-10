n = int(input())
person = []
for _ in range (n):
    person.append(tuple(input().split()))
person.sort(key = lambda x : (-int(x[1]),-int(x[2]),-int(x[3])))
for a in person:
    print(*a)