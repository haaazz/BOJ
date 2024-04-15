# 크루스칼 !!

# find 함수: x의 루트 노드 찾기
def find(x):
    if parents[x] == x:  # x의 부모 노드가 자기 자신이면
        return x        # x는 루트 노드
    
    # 경로 압축(Path Compression)을 위해 부모 노드를 찾아 업데이트
    parents[x] = find(parents[x])
    return parents[x]

# union 함수: 두 노드를 연결하는 함수
def union(x, y):
    x = find(x)  # x의 루트 노드를 찾기
    y = find(y)  # y의 루트 노드를 찾기
    
    if x == y:   # 두 노드의 루트 노드가 같으면(이미 연결되어 있으면) 아무일도일어나지안앗다 !
        return
    
    # 더 작은 루트 노드를 가진 쪽이 대표
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
    
# 가중치를 기준으로 간선 오름차순
edges.sort(key = lambda x: x[2])

hap = 0  # 가중치 합 저장 변수
parents = [i for i in range(V+1)]  # 각 정점의 부모 노드를 저장할 리스트 / 자기 자신으로 초기화

for s, e, w in edges:
    if find(s) == find(e):  # 두 정점이 같은 집합에 속해 있다면 사이클을 형성 -> 무시
        continue
    union(s, e)  # 두 정점 연결
    hap += w

print(hap)