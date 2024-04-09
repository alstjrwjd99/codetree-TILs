class Bomb:
    def __init__(self,code, color, second):
        self.code = code
        self.color = color
        self.second = second

a = input().split()
b = Bomb(a[0],a[1],a[2])
print('code :',b.code)
print('color :',b.color)
print('second :',b.second)