n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def nm(s):
    if len(ans) == m :
        print(*ans)
        return
    
    for i in range(s, len(arr)):
        if arr[i] not in ans:
            ans.append(arr[i])
            nm(i+1)
            ans.pop()

nm(0)