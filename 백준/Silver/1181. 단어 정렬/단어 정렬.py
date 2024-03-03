import sys
input = sys.stdin.readline
a = []

for _ in range(int(input())):
    s = input()
    if s not in a:
        a.append(s)

a.sort()
a.sort(key = len)

for i in a:
    print(i.rstrip())