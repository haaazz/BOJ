n, k = map(int, input().split())  # 물품의 수, 버틸 수 있는 무게
arr = [(0, 0)]
chart = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

for i in range(1, n + 1):   # 물건 하나씩
    for j in range(1, k + 1):  # 1~k무게까지 표 작성
        w = arr[i][0]
        v = arr[i][1]
        if j < w:   # 해당 물건이 더 큰 경우, 이전 표값으로 넣기
            chart[i][j] = chart[i - 1][j]
        else:   # 해당 물건이 들어가는 사이즈인 경우
            chart[i][j] = max(chart[i - 1][j], v + chart[i - 1][j - w])    # 이전 값과 비교

print(chart[n][k])



'''
냅색(Knapsack) 알고리즘

dp[i][j] = max(현재 물건 가치 + dp[이전 물건][현재 가방 무게 - 현재 물건 무게], dp[이전 물건][현재 가방 무게])

물건을 배낭에 담을 때,
① 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
② 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다
    2-1) 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
    2-2) 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.
'''