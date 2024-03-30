import heapq

def ejoong(heap):
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)

for _ in range(int(input())):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [0] * k

    for i in range(k):
        q, n = input().split()
        if q == 'I':    # 삽입
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, (-int(n), i))
            visited[i] = True
        if q == 'D':    # 삭제
            if n == '1' and max_heap:   # 최대값 삭제
                visited[max_heap[0][1]] = 0 # 해당 인덱스 방문 취소
                heapq.heappop(max_heap) # 최대힙에서 삭제
            if n == '-1' and min_heap:
                visited[min_heap[0][1]] = 0
                heapq.heappop(min_heap)
        ejoong(max_heap)    # 정리
        ejoong(min_heap)    # 정리

    # 최대나 최소 힙 비어있으면 엠티 출력
    if not max_heap or not min_heap:
        print('EMPTY')
    # 최대 최소 값 출력
    else:
        print(-max_heap[0][0], min_heap[0][0])