n, m = map(int, input().split())
ans = []

def nm(startnumber):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(startnumber, n+1):
        if i not in ans: 
            ans.append(i)
            nm(i+1)
            ans.pop()

nm(1)