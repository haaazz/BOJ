for testcase in range(3):
    t = int(input())
    sum = 0
    for tc in range(t):
        number = int(input())
        sum += number

    if sum < 0 :
        print('-')
    elif sum == 0 :
        print(0)
    else:
        print('+')