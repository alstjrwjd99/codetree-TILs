n,k,T = input().split()
word = []
for _ in range (int(n)):
    string = input()
    if string[:len(T)] == T:
        word.append(string)
word.sort()
print(word[int(k)-1])