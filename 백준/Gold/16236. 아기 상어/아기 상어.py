# 물고기 m마리 한칸 물고기 하나 필수 애들 크기는 자연수 최초 상어 크기 2 1초에 상하좌우 한칸씩 이동 가능
# 자기보다 큰 물고기 칸 지나갈 수 x
# 더 먹을수없으면 엄마 소환 먹을수있는거 여러개면 가장 가까운거 먹으러감 , 위 - 가장왼쪽
# 레벨=경험치되면 레벨업함 ex 2렙2경험치되면 3렙0경험치됨

# 먹을 수 있는데 최단거리를 찾자
# 먹을 수 있다 = 크기 작음, 갈수 있음

from collections import deque

n= int(input())

#아기상어[크기,경험치] 와 아기상어 위치
shark=[2,0]
shark_location=[]
#아기상어 움직인 수
move_count=0

#배열 초기화
num_list=[]
for i in range(n):
    temp_list=list(map(int,input().split()))
    num_list.append(temp_list)
    #상어 찾기
    if 9 in temp_list:
        for j in range(n):
            if temp_list[j]==9:
                shark_location=[i,j]

#상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#bfs 
def bfs(min_x,min_y,visited,shark):
    shark_x,shark_y=shark_location[0],shark_location[1]
    #샤크의 x,y , 움직인 거리, 샤크의 크기 
    q = deque([[shark_x,shark_y,0,shark[0]]])
    visited[shark_x][shark_y] = True
    while q:
        cur = q.popleft()
        # 목적지 도달한 경우 (BFS는 현재가 항상 최적 경로임을 보장)
        # cur[0]=x좌표 cur[1]=y좌표 cur[2]=움직인 거리
        if cur[0]==min_x and cur[1]==min_y :
            #움직인 거리 리턴
            return cur[2]
        #방향대로 움직임
        for i in range(4):
            nx = dx[i] + cur[0]
            ny = dy[i] + cur[1]
            # print(nx,ny)
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and num_list[nx][ny]<=cur[3]:
                visited[nx][ny] = True
                q.append([nx,ny,cur[2]+1,cur[3]])
    return

while(True):
    #방문지
    
    #최소 움직임
    min=9999  
    min_x=-1
    min_y=-1
    #먹을 수 있는 가장 가까운 물고기 찾기
    for i in range(n):
        for j in range(n):
            visited=[[False for i in range(n)]for j in range(n)]    
            move=bfs(i,j,visited,shark)
            # print(move)
            #해당 좌표의 값이 0이 아니고 상어 렙보다 낮고, 거리가 None(못갔다)가 아니고, 거리가 최소일때
            if 0<num_list[i][j]<shark[0] and move != None and min>move:
                min_x=i
                min_y=j
                min=move
    if min_x==-1 and min_y==-1:
        print(move_count)
        break
    if shark[1]+1==shark[0]:
        shark[0]+=1
        shark[1]=0
    else:
        shark[1]+=1
    num_list[min_x][min_y]=9
    num_list[shark_location[0]][shark_location[1]]=0
    shark_location[0]=min_x
    shark_location[1]=min_y
    move_count+=min