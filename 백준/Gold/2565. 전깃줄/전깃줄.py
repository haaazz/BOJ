# 전깃줄 수
# 전깃줄 연결된 현황
# 전깃줄 개수 - 제일 많이 증가한거 -> 제거해야하는 전깃줄 수

# dp[i] 는 i번째 원소를 마지막 원소로 포함한 부분증가수열 최대 길이

# 감사합니다 센세 | https://www.youtube.com/watch?v=wn2dyWt9ml0
# 주석은 지피티에게

# 최대 길이가 105인 배열 dp를 선언, 초기화
dp = [1 for _ in range(105)]
n = int(input())
ans = []

# 전기줄 시작-끝을 리스트에 추가
for _ in range(n):
    ans.append(list(map(int, input().split())))

# 왼쪽 시작점 기준으로 오름차순 정렬
ans = sorted(ans, key=lambda x: x[0])

# LIS(Longest Increasing Subsequence) 알고리즘을 이용하여 최장 증가 부분 수열의 길이를 계산
for i in range(n):
    for j in range(i):
        # 만약 이전 사건의 종료 시간이 현재 사건의 종료 시간보다 작다면
        if ans[j][1] < ans[i][1]:
            # 현재 사건을 이전 사건의 다음 사건으로 삼아서 최장 부분 수열의 길이를 갱신
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열에서 가장 큰 값이 최장 증가 부분 수열의 길이
# 이를 이용하여 최장 증가 부분 수열의 길이를 cnt에 저장
cnt = max(dp)

# n에서 최장 증가 부분 수열의 길이를 뺀 값을 출력
print(n - cnt)