A = input()
B = [0] * len(A)
value = 0
for i in range (len(A)-1,0,-1):
    if (A[i-1] + A[i]) == '))':
        value += 1
    B[i] = value

answer = 0
for i in range (1,len(A)):
    if (A[i-1] + A[i]) == '((':
        answer+=B[i]
print(answer)