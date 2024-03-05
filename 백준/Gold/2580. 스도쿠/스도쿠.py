# 백트래킹 싫어요
arr = [list(map(int, input().split())) for _ in range(9)]

# i 번 행 j 여부 확인
visited1 = [[False] * 9 for _ in range(9)]
# i 번 열 j 여부 확인
visited2 = [[False] * 9 for _ in range(9)]
# i 번 33사각형 j 여부 확인
visited3 = [[False] * 9 for _ in range(9)]

# 33 정사각형은 각각 33씩 묶어서 처리 사실 이부분 잘 몰라서 친구한테 물어봄,,
def box(i, j):
    return i//3*3 + j//3

for i in range(9):
    for j in range(9):
        if arr[i][j]:
            # 1부터 9까진데 인덱스는 0-8 이라 -1 처리
            visited1[i][arr[i][j]-1] = True
            visited2[j][arr[i][j]-1] = True
            visited3[box(i, j)][arr[i][j]-1] = True

# 백트래킹
def back(i, j):
    # ( 9, 0 ) 이 호출되면 빽트래킹
    if i == 9:
        return True
    
    # 이미 칸이 채워져있다면 빽트래킹 안해도 되니까 다음 칸으로 보내줌
    # 그냥 j를 1씩 더해주면 안됨 (개빡침)
    if arr[i][j]:
        return back(i+(j+1)//9 , (j+1)%9)
    
    for k in range(9):
        # k가 포함되어있으면 무시하고 지나감
        if visited1[i][k] or visited2[j][k] or visited3[box(i, j)][k]:
            continue
        # 새로운 숫자면 추가함 위에서 -1처리한것의 반대로 얘는 숫자값을 넣는거라 +1 처리
        arr[i][j] = k + 1
        visited1[i][k] = visited2[j][k] = visited3[box(i, j)][k] = True
        if back(i+(j+1)//9 , (j+1)%9):
            # 백트래킹이 답을 찾았으면 트루 반환과 동시에 아르르 원복 안함
            return True
        # 내가 했던 모든 깊은 백트래킹에 인해 변환된 아르르를 원복해둠
        arr[i][j] = 0
        visited1[i][k] = visited2[j][k] = visited3[box(i, j)][k] = False
    return False        # 못찾았으면 뽈스 반환~

back(0, 0)
for x in arr:
    print(*x)