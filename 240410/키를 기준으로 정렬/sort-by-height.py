n = int(input())
person = []
for _ in range (n):
    person.append(tuple(input().split()))
person.sort(key = lambda x : x[1])
for a in person:
    print(*a)