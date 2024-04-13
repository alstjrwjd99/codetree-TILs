n = int(input())
cmd = []
for _ in range (n):
    cmd.append(list(input().split()))
has = dict()
for c in cmd:
    if c[0] == 'add':
        has[c[1]] = c[2]
    elif c[0] == 'find':
        if c[1] in has:
            print(has[c[1]])
        else :
            print(None)
    elif c[0] == 'remove':
        has.pop(c[1])