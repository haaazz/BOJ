# 총 n개의 강의, m개의 블루레이
n, m = map(int,input().split())
boon = list(map(int,input().split()))

# 최소값은 가장 긴 영상
start = max(boon)
# 최대값은 다 더한거
end = sum(boon)

# 츄러스친구문제!!!! 이분 탐색
while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 1

    for t in boon:
        # 현재 블루레이에 강의 더 더하면 용량 넘치는지 화긴
        if total + t > mid:
            # 블루레이 넘겨야해서 블루레이 넘버 넘겨주고 시간 초기화
            count += 1
            total = 0
        total += t 

    # 블루레이 개수가 설정 개수 이하면
    if count <= m:
        # 더 담을 수 있으니 범위 바꾸기
        ans = mid
        end = mid - 1
    # 설정 개수 초과면
    else:
        # 시작범위 바꾸기
        start = mid + 1
    
print(ans)