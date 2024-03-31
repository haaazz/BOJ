# nCk = n! / (k! * (n-k)!)

n, k = map(int, input().split())

# a는 분자, b는 분모
a, b = 1, 1

# n부터 n-k+1까지의 곱
for i in range(k):
    a *= n - i

# 1부터 k까지의 곱
for i in range(k):
    b *= (i + 1)

print((a//b) % 10007)