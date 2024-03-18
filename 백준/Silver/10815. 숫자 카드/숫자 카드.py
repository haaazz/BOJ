n = int(input())
narr = set(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))

for i in range(m):
    if marr[i] in narr : 
        print(1, end=' ')
    else : print(0, end=' ')