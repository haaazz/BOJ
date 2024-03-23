n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def nm():
    if len(ans) == m :
        print(*ans)
        return
    
    for i in range(len(arr)):
        ans.append(arr[i])
        nm()
        ans.pop()

nm()