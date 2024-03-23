n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
visited = [0] * n

def nm():
    if len(ans) == m :
        print(*ans)
        return
    
    check = 0
    for i in range(len(arr)):
        if visited[i] == 0 and check != arr[i]:
            ans.append(arr[i])
            visited[i] = 1
            check = arr[i]
            nm()
            visited[i] = 0
            ans.pop()
nm()