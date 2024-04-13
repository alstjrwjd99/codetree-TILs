from collections import Counter

n = int(input())
color = []
for _ in range (n):
    color.append(input())

c = Counter(color)
print(c[max(c)])