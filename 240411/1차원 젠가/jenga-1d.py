n = int(input())
block = []
for _ in range(n):
    tmp = int(input())
    block.append(tmp)
copy_block = []

start, end = tuple(map(int,input().split()))
for i in range (n):
    if not start-1 <= i <= end-1:
        copy_block.append(block[i])
another = []
start, end = tuple(map(int,input().split()))
for i in range (len(copy_block)):
    if not start-1 <= i <= end-1:
        another.append(copy_block[i])
print(len(another))
for a in (another):
    print(a)