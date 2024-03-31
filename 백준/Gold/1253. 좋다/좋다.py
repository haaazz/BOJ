n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for i in range(n):
    tmp = arr[:i] + arr[i + 1:]
    l, r = 0, len(tmp) - 1

    while l < r:
        total = tmp[l] + tmp[r]
        if total == arr[i]:
            cnt += 1
            break

        if total < arr[i]:
            l += 1
        else:
            r -= 1

print(cnt)
