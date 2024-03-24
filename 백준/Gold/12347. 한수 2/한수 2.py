# i는 첫 숫자
# j는 등차

n=int(input())
ans=[]

# i는 첫번째 수
for i in range(1,10):

    if i<=n:
        ans.append(i)
    #j는 등차
    for j in range(9):
        #초기값 설정
        num=str(i)
        #등차대로 증가하는 값
        next=i+j

        #1~9까지 넣어주기

        #next가 9보다 커지거나 num이 n보다 커질 때 부레키
        while(True):
            if next>9:
                break
            num=num+str(next)
            if int(num)>n:
                break
            elif int(num) not in ans:
                ans.append(int(num))
            next=next+j


for k in range(1,10):
    # for l in range(9):
    for l in range(10):
        num=str(k)
        next=k-l
        while(True):
            if next<0:
                break
            num=num+str(next) 
            # print(num)
            if int(num)>n:
                break
            elif int(num) not in ans:
                ans.append(int(num))
            next=next-l
# print(sorted(ans))
print(len(ans))
# print(ans)