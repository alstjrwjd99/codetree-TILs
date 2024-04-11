A = input()

def encolen(A):
    en = A[0]
    cnt = 0
    for a in A:
        if en[-1] != a:
            en += str(cnt) + a
            cnt = 1
        else :
            cnt += 1
    return en + str(cnt)
answer = 1000000000
for i in range (len(A)):
    b = A[i:] + A[:i]
    answer = min(len(encolen(b)),answer)
print(answer)