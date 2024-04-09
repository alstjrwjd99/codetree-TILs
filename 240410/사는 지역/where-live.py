class Person:
    def __init__(self,name, address, area):
        self.name = name
        self.address = address
        self.area = area
n = int(input())
p = []
for _ in range (n):
    a = input().split()
    b = Person(a[0],a[1],a[2])
    p.append(b)
p.sort(key = lambda x : x.name,reverse = True)

print('name',p[0].name)
print('addr',p[0].address)
print('city',p[0].area)