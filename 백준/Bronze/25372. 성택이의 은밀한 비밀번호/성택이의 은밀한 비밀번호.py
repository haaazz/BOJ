n = int(input())
for i in range(n):
    str = input()
    if len(str) >= 6 and len(str) <= 9:
        print('yes')
    else:
        print('no')