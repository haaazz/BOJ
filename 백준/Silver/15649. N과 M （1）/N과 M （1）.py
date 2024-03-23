n, m = map(int, input().split())
result = []

def back():
    if len(result) == m: #배열의 길이가 우리가 찾고자 하는 그 길이라면
        print(" ".join(map(str, result))) # 출력 형태를 맞춰주려고 함, 리스트 요소를 문자열 형태로, 사이 공백
        return
    
    for i in range(1, n+1): # 1부터 n까지 자연수의 범위
        if i not in result: # 중복이 없어야하므로 result내에 이미 있는 요소가 아니라면
            result.append(i)
            back() # 재귀, 일종의 반복
            result.pop() # 재귀 후 return되면 여기로 돌아와서 마지막 요소 제거 - 그래야 같은 레벨 다른 가지 넣을 수 있음

back() # 함수 호출