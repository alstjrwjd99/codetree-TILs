class Bomb:
    def __init__(self,code=50, product = 'codetree'):
        self.code = code
        self.product = product
c = Bomb()
print('product',c.code,'is',c.product)

a = input().split()
b = Bomb(a[1],a[0])

print('product',b.code,'is',b.product)