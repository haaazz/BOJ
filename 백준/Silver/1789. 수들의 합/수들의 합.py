# n이 자연수 개수, 합이 s
# 이진탐색 좋아좋아
# 수가 매우 크기때문에-42억- 완탐하면 터짐

def bs(start, end, s, answer):
    if start > end:
        return answer
    mid = (start+end)//2
    sum = (mid*(mid+1))//2
   
    if sum > s:
        return bs(start, mid-1, s, mid-1)
    else:
        return bs(mid+1, end, s, answer)

s = int(input())
print(bs(0, s, s, 1))