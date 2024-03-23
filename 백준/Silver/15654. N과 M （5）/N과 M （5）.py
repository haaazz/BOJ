n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def nm():
    if len(ans) == m :
        print(*ans)
        return
    
    for i in range(len(arr)):
        if arr[i] not in ans:
            ans.append(arr[i])
            nm()
            ans.pop()

nm()