# 이 문제가 dx dy가 아니라니?? 풍선팡이랑 똑같이생겼는데 ....
# 시간 제한 1초에 n이 10만까지 주어짐 -> 완탐(2의n승)하면 터진다는 뜻 !

# DP 이용 -> 본인의 스티커 값과 그 이전 열의 대각선 dp값을 합쳐서 저장
# 1열 전의 대각선 dp 값을 더하는 것보다 2열 전의 대각선 행의 dp 값을 더하는것이 더 크다면 2열전의 dp값을 더해주는 예외처리


t = int(input())  # 테스트 케이스의 수를 입력 받음
for _ in range(t):
    stickers = []  # 스티커를 담을 리스트
    n = int(input())  # 스티커의 개수를 입력 받음
    for i in range(2):
        temp = list(map(int, input().split()))  # 한 줄에 있는 스티커의 점수를 입력 받아서 리스트로 변환
        stickers.append(temp)  # 스티커 리스트에 추가
    
    # 동적 계획법을 위한 2차원 배열 초기화
    dp = [[0 for i in range(n)], [0 for i in range(n)]]
    
    # 첫 번째 열에 스티커의 점수 미리 저장
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    
    if n > 1:  # 스티커가 1개 이상일 경우
        # 두 번째 열에 스티커의 점수 입력
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]

    # 최대 점수 계산
    for i in range(2, n):  # 세 번째 열부터 마지막 열까지
        for j in range(0, 2):  # 0행과 1행을 번갈아가며
            # j의 값을 반전 - j가 0이면 1이 되고, 1이면 0
            # 무조건 행의 대각선 한칸 / 두칸 옆으로 가고, 스위칭으로 위아래 바꿔주기
            a = dp[1 - j][i - 1] + stickers[j][i]  # 전칸 대각선
            b = dp[1 - j][i - 2] + stickers[j][i]  # 두번째 전칸 대각선
            dp[j][i] = max(a, b)  # 두 경우 중 최대 점수를 선택하여 dp에 저장

    # 결과 출력
    print(max(dp[1][-1], dp[0][-1]))  # 마지막 열의 최대 점수 출력