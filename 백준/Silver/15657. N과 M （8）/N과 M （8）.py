n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def nm(start):
    if len(ans) == m :
        print(*ans)
        return
    
    for i in range(start, len(arr)):
        ans.append(arr[i])
        nm(i)
        ans.pop()
nm(0)