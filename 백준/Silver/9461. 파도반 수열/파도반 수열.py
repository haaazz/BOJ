# 바로 전 삼각형 수 + 5번 전 삼각형 수 = 자기 자신의 삼각형 수

# 맨 첫번째는 패딩
dp = [0, 1, 1, 1, 2, 2]

for _ in range(95): # n 범위가 100까지라서
    dp.append(dp[-1] + dp[-5])

for _ in range(int(input())):
    print(dp[int(input())])