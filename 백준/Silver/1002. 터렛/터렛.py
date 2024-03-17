# 평면 좌표에서 두 점 사이의 거리 구하기
# 원 두 개가 외접하는지 내접하는지 안만나는지로 나눠야함
# r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if dist == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == dist or r1 + r2 == dist:  # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < dist < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외