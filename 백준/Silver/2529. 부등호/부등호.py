k = int(input())
mark = list(map(str, input().split()))  # 부등호 입력받는거
result = []
visited = []

def check(left, sign, right): #왼쪽 숫자, 오른쪽 숫자, 부등호
    if sign == '<':
        return left < right
    else:
        return left > right 

def back(count, temp_list): # count - 정수가 재귀된 횟수
    if count == k + 1:    # 부등호가 2개라면 숫자는 3개여야함, 부등호가 k개면 숫자는 k+1개
        a = ''
        for i in temp_list:
            a = a + str(i)
        result.append(a)
        return
    
    
    for i in range(10):
        if i not in visited: # 중복이 안돼            
        # temp_list가 비어서 0이 돌려지면 오류가 발생하므로 0 처리하는걸 생각해야했음
            if count == 0 or check(temp_list[-1], mark[count-1], i):
                visited.append(i)
                temp_list.append(i)
                back(count+1, temp_list)
                visited.pop()
                temp_list.pop()
back(0, [])
print(result[-1])   # 가장 큰 수
print(result[0])    # 가장 작은 수