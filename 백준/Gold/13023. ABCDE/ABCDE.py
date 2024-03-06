# a-b-c-d-e 노드 연결되어야함 -> dfs로 레벨 확인함

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False] * n

# 양방향 리스트여서 (혼자만 친구라고 생각하는건 슬퍼요) 양쪽에 입력
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(curr, level):
    """
    curr : 현재 노드의 인덱스
    level : 현재까지의 깊이 레벨
    """
    if level == 4: # 조건대로 다 연결됐으면
        print(1)
        exit()
    for i in arr[curr]: # 현재 노드와 연결된 노드들
        if not visited[i]:  
            visited[i] = True   # 방문하면 방문표시
            dfs(i, level + 1)   # 방문한곳에서 dfs 이어서
            visited[i] = False  # 탐색 끝나면 방문표시 해제

# 노드를 순서대로 방문하며 dfs를 수행
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)