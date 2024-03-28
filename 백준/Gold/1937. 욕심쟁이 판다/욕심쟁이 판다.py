import sys

sys.setrecursionlimit(400000)

# 모든 점을 방문
# 방문한 뒤에 이동할 수 있는 모든 경우의 수 재귀로 구현 -> DFS
# 재귀로 구현한 뒤 DP로 변환

def panda(y, x):

    # 방문했던 dp면 dp값 가져오기
    if dp[y][x] != 0:
        return dp[y][x]

    for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]]:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < n:
            if graph[y][x] < graph[ny][nx]:
                dp[y][x] = max(dp[y][x], panda(ny, nx) + 1)

    return dp[y][x]    # 이동 불가하면 0

n = int(input())    # 그래프의 크기

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]


for y in range(n):
    for x in range(n):
        panda(y, x)

print(max(map(max,dp)) + 1)
