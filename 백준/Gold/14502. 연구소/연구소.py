# 상하좌우 다 퍼져나가는 바이러스, 벽은 무조건 세개 세워야함, 벽 세우고 바이러스 못오는곳은 안전한곳, 안전한곳 최대값

from collections import deque

def bfs(tlist):
    # 벽 세우기
    for i, j in tlist:
        arr[i][j] = 1

    # 변수, 큐 만들기, 초기화
    q = deque()
    v2 = [[0] * m for _ in range(n)]
    Cnt = cnt-3 # 남은 0의 개수

    for ti, tj in virus:
        q.append((ti, tj))
        v2[ti][tj] = 1

    # 큐에 데이터 있는동안 하나씩 꺼내서 처리
    while q:
        ci, cj = q.popleft()
        # 네 방향, 범위 내, 미방문, 조건 ==0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and  0 <= nj < m and v2[ni][nj] == 0 and arr[ni][nj] == 0:
                v2[ni][nj] = 1
                q.append((ni, nj))
                Cnt -= 1
            
    # 벽 부수기
    for i, j in tlist:
        arr[i][j] = 0
    return Cnt

def dfs(n, tlist):
    global dap
    if n == 3:
        dap = max(dap, bfs(tlist))
        return
    
    for j in range(cnt):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, tlist+[binkan[j]])
            v[j] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

binkan = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            binkan.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

cnt = len(binkan)
v = [0] * cnt
dap = 0


dfs(0, [])
print(dap)