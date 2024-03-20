'''
따봉구글 따봉지피티야 고마워 !!

힙은 일반적으로 가장 작은(또는 가장 큰) 요소에 대한 빠른 접근을 제공하며, 요소를 추가하거나 제거하는 데에도 효율적입니다.
따라서 힙을 사용하여 입력된 숫자 중에서 상위 n개의 숫자를 유지하면서
새로운 숫자가 추가될 때마다 기존의 가장 작은 숫자를 제거하여 상위 n개의 숫자를 유지할 수 있습니다.
이를 통해 메모리 사용량을 줄이고, 계산을 효율적으로 수행할 수 있습니다.
'''

import heapq

hp = []
n = int(input())

for _ in range(n):
    num = map(int, input().split())
    for number in num:
        if len(hp) < n:  # 힙의 크기를 n개로 유지
            heapq.heappush(hp, number)
        else:
            if hp[0] < number:  # 힙의 최솟값보다 큰 경우
                heapq.heappop(hp)  # 힙의 최솟값을 제거
                heapq.heappush(hp, number)  # 새로운 숫자를 삽입
# 결과 출력
print(hp[0])  # 힙의 최솟값 출력