def bs(x):
    # 시작점끝점
    s, e = 0, n - 1
    # end start 차이가존재할때까지
    while s <= e:
        # 중앙값 설정
        mid = (s + e) // 2
        # 중앙값이랑 타겟이 같으면 true
        if narr[mid] == x:
            return 1
        # 중앙값이 타겟보다 크면 끝값 땡겨오기 (왼쪽 탐색)
        elif narr[mid] > x:
            e = mid - 1
        else:
            s = mid + 1
    # 못찾으면 false
    return 0

t = int(input())
for tc in range(t):
    n = int(input())
    narr = list(map(int, input().split()))
    m = int(input())
    marr = list(map(int, input().split()))
    narr.sort()
    for i in marr:
        print(bs(i))