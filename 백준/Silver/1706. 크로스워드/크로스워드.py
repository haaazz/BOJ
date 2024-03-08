r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
wordlist = []

# 가로 단어 탐색
for i in range(r):
    word = ''
    for j in range(c):
        if arr[i][j] != '#':
            word += arr[i][j]
        else:
            if len(word) >= 2:
                wordlist.append(word)
            word = ''
    if len(word) >= 2:  # 마지막 단어 처리
        wordlist.append(word)

# 세로 단어 탐색
for i in range(c):
    word = ''
    for j in range(r):
        if arr[j][i] != '#':
            word += arr[j][i]
        else:
            if len(word) >= 2:
                wordlist.append(word)
            word = ''
    if len(word) >= 2:  # 마지막 단어 처리
        wordlist.append(word)

wordlist.sort()
print(wordlist[0])  # 사전식 순으로 가장 앞선 단어 출력