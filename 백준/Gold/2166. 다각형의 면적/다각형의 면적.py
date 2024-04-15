# ...이런 수학문제 너무하다고 생각해
# 참고 링크 https://darkpgmr.tistory.com/86

n = int(input())
xlist = []
ylist = []
for _ in range(n):
    x,y = map(float,input().split())
    xlist.append(x)
    ylist.append(y)
xlist.append(xlist[0])
ylist.append(ylist[0])
area = 0
# print(x_list,y_list)
for i in range(n):
    temp_area = (xlist[i] * ylist[i+1]) - (xlist[i+1] * ylist[i])
    area += temp_area
print(abs(area)/2)