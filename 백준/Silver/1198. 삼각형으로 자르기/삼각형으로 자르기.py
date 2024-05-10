# N각형에서 나오는 삼각형의 경우의 수nC3 => n(n-1)(n-2)/6

from itertools import combinations

def tri(x, y, z):
    return abs((x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-x[1]*y[0]-y[1]*z[0]-z[1]*x[0]))/2

spot = []
max_ = []
a = []

for i in range(int(input())):
    spot.append(list(map(int, input().split())))
    
spots = list(combinations(spot, 3))
for k in range(len(spots)):
    max_.append(tri(spots[k][0], spots[k][1], spots[k][2]))
print(max(max_))