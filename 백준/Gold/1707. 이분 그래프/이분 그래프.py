# 이분그래프? -> 인접한 정점끼리 다른 색으로 칠해서 모든 정점을 두가지 색으로만 칠할 수 있는 그래프
# DFS, BFS를 통해서 판별 가능함

import sys
sys.setrecursionlimit(10**5)

# dfs
def dfs(v, color):
    visit[v] = color  # 방문한 v에 색상 부여

    for i in graph[v]:
        if visit[i] == 0:  # 아직 방문 안했으면
            if dfs(i, -color):  # 방문해서 다른 색상 부여
                pass
            else:
                return False
        elif visit[i] == visit[v]:  # i를 방문했는데 v랑 색이 같으면 이분그래프 아님
            return False
    return True  # 이분 그래프 확인 완료

k = int(sys.stdin.readline())

for _ in range(k): # 테스트 케이스
    V, e = map(int, sys.stdin.readline().split()) # V 노드 e 간선
    graph = [[] for _ in range(V + 1)]  # 인접리스트
    visit = [0] * (V + 1)
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)

    eboon = True  # 이분그래프인지 확인

    for i in range(1, V + 1):
        if visit[i] == 0:  # 미방문 정점 기준으로 dfs 실행
            eboon = dfs(i, 1)   # 시작 정점 색상 부여
            if not eboon:
                break   # 이분 그래프 아니면

    print("YES" if eboon else "NO")