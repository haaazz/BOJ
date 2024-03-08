from collections import deque


def bfs(dx,dy,start,visited,count):
    # 이차원 리스트안에 start[0](상의 x좌표) start[1](상의 y좌표), count(이동횟수) 넣어줌
    q =deque([[start[0],start[1],count]])
    # 상 방문 좌표 처리
    visited[start[0]][start[1]]=True
    while q:
        v= q.popleft()
        # dx,dy 횟수만큼 빙빙돌아
        for i in range(8):
            # block 다른 장기말이랑 겹치는 여부 파악
            block=False
            x=v[0]
            y=v[1]
            # print(x,y)
            for j in range(3):
                # print(i,j,dx[i][j])
                x=x+dx[i][j]
                y=y+dy[i][j]
                if x==kingx and y==kingy and j !=2:
                    block=True
            if block==True:
                continue
                
            if x>=0 and x<10 and y>=0 and y<9 and visited[x][y]==False:
                # 만약 움직인 값이 킹의 위치와 같으면 그동안의 반복 횟수(v[2],3번에 처음에 넣어줬던 count)리턴
                if x==kingx and y==kingy:
                    return v[2]
                else:
                    q.append([x,y,v[2]+1])
                    visited[x][y]=True

    return -1

#세로,가로
n=10
m=9

#방문여부
visited=[[False]*m for _ in range(n)]

#상,왕의 x,y
sangx,sangy=map(int,input().split())
kingx,kingy=map(int,input().split())

#횟수
count=1

#상좌,상우,하좌,하우,좌상,좌하,우상,우하
dx=[[-1,-1,-1], [-1,-1,-1], [1,1,1], [1,1,1], [0,-1,-1], [0,1,1], [0,-1,-1], [0,1,1]]
dy=[[0,-1,-1], [0,1,1], [0,-1,-1], [0,1,1], [-1,-1,-1], [-1,-1,-1], [1,1,1], [1,1,1]]

#bfs 시작 지점
start=[sangx,sangy]
print(bfs(dx,dy,start,visited,count))