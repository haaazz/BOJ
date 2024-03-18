# x-1 x+1 1초 x*2 0초 최소이동시간 x*2에 가중치둘것 (시간 최소)

from collections import deque  
  
def bfs(s):  
    vi = [float('inf')] * 100001  
    vi[s] = 0  
    q = deque()  
    q.append(s)  
    while q:  
        cur = q.popleft()  
        for i in (cur+1,cur-1, cur*2):  
            if 0<=i<100001:  
                if i == cur * 2:  
                    if vi[i] > vi[cur]:  
                        vi[i] = vi[cur]  
                        q.append(i)  
                else:  
                    if vi[i] > vi[cur] + 1:  
                        vi[i] = vi[cur] + 1  
                        q.append(i)  
    # print(vi)  
    return vi[k]  
n, k = map(int, input().split())  
  
if k <= n:  
    print(n - k)  
else:  
    print(bfs(n))