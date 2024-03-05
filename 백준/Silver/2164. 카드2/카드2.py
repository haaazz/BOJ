from collections import deque

n = int(input())
dq = deque()
for i in range(1, n+1):
    dq.append(i)


for j in range(n-1):
    dq.popleft()
    new = dq.popleft()
    dq.append(new)

print(*dq)