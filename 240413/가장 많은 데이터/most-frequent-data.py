# 변수 선언 및 입력:
n = int(input())
words = [input() for _ in range(n)]

freq = dict()
ans = 0

# 각 문자열이 몇 번씩 나왔는지를
# hashmap에 기록해줍니다.
for word in words:
    # 처음 나온 문자열이라면 1을 직접 적어줘야 합니다.
    if word not in freq:
        freq[word] = 1
    # 이미 나와있던 문자열이라면 1을 더해줍니다.
    else:
        freq[word] += 1

    # 가장 많이 나온 횟수를
    # 갱신해줍니다.
    ans = max(ans, freq[word])

print(ans)