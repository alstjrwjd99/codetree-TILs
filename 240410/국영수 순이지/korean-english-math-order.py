n = int(input())
person = []
for _ in range (n):
    person.append(tuple(input().split()))
person.sort(key = lambda x : (x[1],x[2],x[3]),reverse = True)
for a in person:
    print(*a)