# 배열 전체를 더하고 n년후 빙하를 bfs에 돌렸는데 값이 배열 전체 값보다 작으면 덩이가 나눠진것임
# 1년마다 그래프 전체 값 더하고 -> bfs돌려서 값 비교

# 입력 세로 가로 n m

from collections import deque

n,m=map(int,input().split())
#빙산 리스트 생성
ice_list=[]
num=0
for i in range(n):
    m_list=list(map(int,input().split()))
    ice_list.append(m_list)
    num=num+sum(m_list)


#bfs 
def bfs(start_x, start_y, graph,num):
    
    #상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    #비교할 합
    temp_sum=0
    #내년의 합
    next_sum=0
    #첫번째 노드를 덱에 넣어줌
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])


    # print(graph)
    while queue:
        #현재 맨 왼쪽 노드를 덱에서 뽑아줌 (여기서 시작이니까)
        x, y = queue.popleft()
        temp_sum+=graph[x][y]

        zero_count=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny]==0:
                zero_count+=1
            elif graph[nx][ny]!=0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        #내년 리스트 값 넣어주기
        next=ice_list[x][y]-zero_count
        if next>0:
            next_year[x][y]=next
            next_sum+=next
    # print(temp_sum,num)
    if temp_sum!=num:
        return -1
    return next_sum


#년 수 
year=0
#bfs로 년 수 카운팅
while(True):
    #내년 리스트
    next_year=[[0 for i in range(m)] for j in range(n)]
    #빙산에서 0이 아닌 수를 찾음.
    x=-1 
    y=-1
    for i in range(n):
        for j in range(m):
            if ice_list[i][j]!=0:
                x,y=i,j
                
    #리스트가 다 0이면
    if x==-1 and y==-1:
        print(0)
        break
    #0이 아닌 수의 x,y로 bfs 시작.
    count=bfs(x,y,ice_list,num)
    
    #정답 출력
    if count==-1:
        print(year)
        break
    else:
        num=count
    ice_list=next_year.copy()
    year+=1