def dfs(q):
    global result
    if q == n:    # 모든 행을 탐색한 경우: 성공
        result += 1
        return

    for j in range(n):  # 행 순차적으로 탐색 ㄱㄱ
        if visited1[j] == visited2[q+j] == visited3[q-j] == 0:  # 열/대각선 충돌 없음 ( 놓을 수 있음 !! )
            visited1[j] = visited2[q + j] = visited3[q - j] = 1   # 열과 대각선 방문 표시
            dfs(q + 1)    # 다음 행 탐색
            visited1[j] = visited2[q + j] = visited3[q - j] = 0   # 되돌아오면서 상태 해제

n = int(input())
result = 0
visited1 = [0]*n  # 열의 방문 여부 저장 리스트
visited2 = [0]*(2*n-1)  # 우하향 대각선 방문 여부 저장 리스트
visited3 = [0]*(2*n-1)  # 좌하향 대각선 방문 여부 저장 리스트
dfs(0)  # 첫번째 행부터 탐색
print(result)  # 찾은 총 개수 출력