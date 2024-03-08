n = int(input())
sb = 0

while n >= 0 :
    if n% 5 == 0:
        sb += int(n/5)
        print(sb)
        break
    n -= 3
    sb += 1
    
    if n < 0:
        print(-1)