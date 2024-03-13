def dfs(n, sm):
    global ans

    if  n >= N:
        ans = max(ans, sm)
        return
    
    if n+t[n] <= N : # 상담하는 경우 퇴사 전에 완료 가능일때만
        dfs(n+t[n], sm+p[n])
    dfs(n+1, sm)    # 상담 안하는경우는 항상 가능하므로 습관성 else에 주의....


N = int(input())
t = [0] * N
p = [0] * N


for i in range(N):
    t[i], p[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)