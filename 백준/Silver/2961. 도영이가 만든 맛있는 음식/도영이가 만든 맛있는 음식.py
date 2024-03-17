from itertools import combinations

n = int(input()) # 재료의 개수 입력
jaeryo = [list(map(int,input().split())) for _ in range(n)] # 재료의 신맛, 쓴맛 이중 리스트
result = 1e9 # 10억으로 초기화
for cmbs in [combinations(jaeryo, i) for i in range(1, n+1)]:
    for c in cmbs:
        S,B=1,0       # 신맛, 쓴맛 초기화
        for s,b in c: # 각 조합에 대해
            S*=s;B+=b # 신맛은 곱하고, 쓴맛은 더한다, 세미콜론 써서 한 줄에 작성하기
        result=min(result, abs(S-B)) # 최소값 갱신
print(result)