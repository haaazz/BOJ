# 구멍의 너비, 조각의 수, 조각 사이즈 (나노미터 ~ 1센치미터 = 10000000나노미터
# 못찾으면 danger 찾으면 yes 조각작은거 조각큰거
# 레고 조각 수 개많음 도라이임 -> 투포인터 ㄱㄱ

while True:
    try:
        x = int(input())*10_000_000
        n = int(input())
        legos=[]
        for _ in range(n):
            legos.append(int(input()))
        legos.sort()

        start = 0 
        end = n - 1 

        while(start <= end):
            mid = (start + end)//2 

            if legos[mid] >= x:
                end = mid-1
            else:
                start = mid+1
        flag = True
        start = 0
        while(start<end): 

            if legos[start] + legos[end] == x: 
                print("yes " + str(legos[start]) + " " + str(legos[end]))
                flag = False
                break 
            elif legos[start] + legos[end] > x: 
                end -= 1
            else:
                start += 1
        if flag:
                print("danger")
    except:
        break