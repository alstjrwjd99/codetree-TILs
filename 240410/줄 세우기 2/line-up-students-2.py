n = int(input())
student = []
for i in range (1,n+1):
    a = tuple(map(int,input().split()))
    student.append((a[0],a[1],i))
student.sort(key = lambda x : (x[0],-x[1]))
for a in student:
    print(*a)