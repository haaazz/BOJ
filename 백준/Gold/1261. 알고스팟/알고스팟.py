# 2차원배열 미로에 갇힘 운영진 여러명은 한명이라고 생각해야함(다같이붙어있으래)
# 벽을 몇개 부숴야하는지!!
# 완탐 -> 백트래킹해서 풀 수는 있지만 ... 터짐 백트래킹 조건 찾기 어려움
# 이사람 시간복잡도 정리 잘해뒀음 보고 배웠다 -> https://developingbear.tistory.com/141

import heapq
 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

M,N = map(int, input().split())
arr = []
for i in range(N):
    temp = input().strip() # "011"
    temp_arr = [] 
    for j in temp: # j= "0","1","1"
        temp_arr.append(int(j)) # temp_arr = [0,1,1]
    arr.append(temp_arr) 
dist = [[1e9 for i in range(M)] for j in range(N)]
dist[0][0] = 0


q = []
#거리,x,y
heapq.heappush(q,[0,0,0])

while q:
    #우선순위 큐로 거리보고 정렬
    weight,x,y = heapq.heappop(q)

    #4방 배열
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 벽이면 arr[nx][ny]가 1 , 아니면 0 이므로 
            # 그대로 부신 벽 수로 더해주면 됨 
            if dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                dist[nx][ny] = dist[x][y] + arr[nx][ny]
                heapq.heappush(q,[weight,nx,ny])
print(dist[N-1][M-1])