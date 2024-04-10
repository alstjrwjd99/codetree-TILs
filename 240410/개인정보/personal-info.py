n = 5
person = []
for i in range (1,n+1):
    person.append(input().split())
person.sort(key = lambda x : (x[0]))
print('name')
for a in person:
    print(*a)
person.sort(key = lambda x : (-1 * int(x[1])))
print('')
print('height')
for a in person:
    print(*a)