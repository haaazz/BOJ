# 한수 1의 경우...
# 1~99는 한수
# 100~1000 = abc일때 a, b 차이랑 b, c 차이 같으면 한수

num = int(input())

hansu = 0

for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1  # 100보다 작으면 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1  # x의 각 자리가 등차수열이면 한수
print(hansu)