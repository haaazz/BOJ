from collections import deque

n, m, r = map(int, input().split())

graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visit = [0] * (n + 1)
count = 1
visit[r] = count

def bfs():
    global count
    q = deque()
    q.append(r)
    while q:
        now = q.popleft()
        for i in sorted(graph[now], reverse=True):
            if visit[i] == 0:
                count += 1
                visit[i] = count
                q.append(i)
bfs()
for i in range(1, n+1):
    print(visit[i])