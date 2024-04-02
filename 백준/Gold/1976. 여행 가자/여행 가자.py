n = int(input())
m = int(input())

# 인접행렬
nara_ya = []
# 방문
visited = [0 for _ in range(n)]
for _ in range(n):
  nara_ya.append(list(map(int,input().split())))
# 출발지
start = list(map(int,input().split()))

def dfs(start):
    visited[start] = 1  # 시작 노드 방문처리
    # 현재 노드랑 연결된 모든 노드
    for index,j in enumerate(nara_ya[start]):
        # 연결된 노드 있고 방문안한경우
        if j == 1 and visited[index] == 0:
          visited[index]=1
          dfs(index)    # 방문표시하고 다시 dfs

dfs(start[0] - 1)   # 함수 실행, 연결 여부 확인

if 0 not in visited:    # 다 방문했으면
  print('YES')
  exit()
for i in start:
  if visited[i - 1] == 0:
    print('NO')
    exit()
print('YES')