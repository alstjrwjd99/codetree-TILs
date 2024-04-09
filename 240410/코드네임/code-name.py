min_name = 0
min_score = 101
for _ in range (5): 
    name,score = input().split()
    if int(score) < min_score:
        min_name = name
        min_score = int(score)
print(min_name,min_score)