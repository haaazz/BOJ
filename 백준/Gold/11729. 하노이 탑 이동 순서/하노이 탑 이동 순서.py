def move(num, start, arrive):
    temp = []
    # 만약 이동할 원반이 1개보다 많다면,
    if num > 1:
        # 중간 기둥을 찾기 위한 반복문
        for i in range(1, 4):
            # 시작 기둥과 도착 기둥이 아닌 다른 기둥을 임시로 저장
            if i != start and i != arrive:
                temp = i
        # 재귀적으로 원반을 중간 기둥으로 이동시키고
        a = move(num-1, start, temp)
        # 가장 큰 원반을 목표 기둥으로 이동시키고
        b = move(1, start, arrive)
        # 중간 기둥에 있는 원반들을 목표 기둥으로 이동시킴
        c = move(num-1, temp, arrive)
        # 원반들의 이동 경로를 합침
        temp = a + b + c
    else:
        # 원반이 1개일 경우에는 바로 시작 기둥에서 도착 기둥으로 이동시킴
        return [start, arrive]
    return temp

# 원반의 개수를 입력받음
n = int(input())
# 이동 경로 계산
ans = move(n, 1, 3)
# 이동 횟수 출력
print(len(ans)//2)
# 이동 경로 출력
for i in range(len(ans)//2):
    print(ans[2*i], end=' ')
    print(ans[2*i+1])