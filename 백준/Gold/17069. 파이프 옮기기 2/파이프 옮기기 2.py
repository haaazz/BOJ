# n * n격자판, r은 행 c는 열
# 벽에 닿으면 안됨
# 45도회전 / 오른쪽 아래 오른쪽아래 -> n, n까지 이동하는 방법의 수

# 풀이를 작성하기에 앞서 빡대가리 하림이를 도와준 싸피 11기 구미6반이었던 이 훈군에게 감사를 표합니다.
# 하림이는 3차원그래프같은거 몰라 -> 가로 세로 대각선DP를 따로 만들자 ~~^^
# 범위 설정을 할 수가 없음... x는0이고 y는아닐때도있고 그래서 그냥 0열 0행을 그냥 아예 따로 처리하고 1, 1부터 for문으로 순회

n=int(input())

#벽은 1 나머지는 0인 그래프
graph=[list(map(int,input().split())) for _ in range(n)]


#가로 세로 대각선 DP 생성 
garo_dp = [[0 for _ in range(n)]for _ in range(n)]
sero_dp = [[0 for _ in range(n)]for _ in range(n)]
daegak_dp =[[0 for _ in range(n)]for _ in range(n)]

#초기의 파이프에 대한 dp 생성
garo_dp[0][1]=1

# print(graph)

#좌 상 상좌 (파이프를 움직일 때 사용)
dx=[0,-1,-1]
dy=[-1,0,-1]

# 1열은 다 0이니까 graph[][]이 인덱스 오버가 나지 않게
# 1행만 따로 처리
# 따로안해두면 if문 개많이쓰고(x가0이고 y가0이지않을때,x가0이고y가0일때 등등..) 
# 각각 경우마다 continue 해야함
# 근데 그래놓고 오답뜸 그냥 이렇게 하세요 쓰러지기 싫으면
for i in range(2,n):
    #가로dp 입력받는데 벽이 없으면
    if graph[0][i]==0 and graph[0][i-1]==0:
        #가로dp를 받는다.
        garo_dp[0][i]=garo_dp[0][i-1]

# x y를 1부터 n까지
for x in range(1,n):
    for y in range(1,n):
         #dp가 모두 0일때 ->한번도 방문하지 않았을 때 + dp가 들렸을수도 있지만 값은 0일 때 
        if garo_dp[x][y]==0 and sero_dp[x][y]==0 and daegak_dp[x][y]==0:

            #왼쪽에서 오는 애 -> 자기 그래프값이 0이면 됨
            if graph[x][y]==0:
                #왼쪽의 가로dp, 대각선dp  가져옴
                garo_dp[x][y]=garo_dp[x+dx[0]][y+dy[0]]+daegak_dp[x+dx[0]][y+dy[0]]
            

            #위에서 오는 애 -> 자기 그래프값이 0이면 됨
            if graph[x][y]==0:
                #위의 세로dp, 대각선dp 가져옴
                sero_dp[x][y]=sero_dp[x+dx[1]][y+dy[1]]+daegak_dp[x+dx[1]][y+dy[1]] 
           

            #대각선에서 오는 애 ->자기랑,자기왼쪽,윗쪽 그래프의 값이 다 0 이여야 됨
            if graph[x][y]==0 and graph[x][y-1]==0 and  graph[x-1][y]==0:
                #대각선의 가로,세로,대각선dp 다 가져옴
                daegak_dp[x][y]=garo_dp[x+dx[2]][y+dy[2]]+sero_dp[x+dx[2]][y+dy[2]]+daegak_dp[x+dx[2]][y+dy[2]]

#마지막 구석자리의 가로,세로,대각선dp값 합친거 출력
print(garo_dp[n-1][n-1]+sero_dp[n-1][n-1]+daegak_dp[n-1][n-1])


''' 다른풀이
https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python
센세 감사합니다
-
설치 가능한 경우
가로 파이프 - 이전 파이프가 가로, 대각선일때
세로 파이프 - 이전 파이프가 세로, 대각선일때
대각선 파이프 - 이전 파이프 모양에 구애받지 x

원래 인덱스 1: dp1 -> 2차원 그래프
지금은 가로 세로 대각선 -> 3차원

# 0 → ─, 1 → /, 2 → |

def solution():

    # 1행 미리 처리하기 → (3) 과정
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
	
    
    # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
    for r in range(1, N):
        for c in range(1, N):
            # (5) 과정
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
                
	    # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
    
    
    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()

'''