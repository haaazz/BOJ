n, m = map(int, input().split())
ans = []

def nm():
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(1, n+1):
        ans.append(i)
        nm()
        ans.pop()

nm()