def cal(alist, blist):
    asum = bsum = 0
    for i in range(m):
        for j in range(m):
            asum += arr[alist[i]][alist[j]]
            bsum += arr[blist[i]][blist[j]]
    return abs(asum - bsum)

def dfs(people, alist, blist):
    global result
    if people == n:
        if len(alist) == len(blist):     # 같은 인원으로 팀을 구성
            result = min(result, cal(alist, blist))
        return
    
    dfs(people+1, alist+[people], blist) # a 팀 선택
    dfs(people+1, alist, blist+[people]) # b 팀 선택


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

m = n//2
result = 100 * m * m
dfs(0, [], [])
print(result)